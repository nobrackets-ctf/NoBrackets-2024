import socket
import threading
import sys
import random
import struct
import time

def usage():
    print("Usage:")
    print("  Serveur : python canal.py serveur <PORT>")
    print("  Client  : python canal.py client <HOST> <PORT>")
    sys.exit(1)

def c(data, rand_gen):
    return bytes([b ^ rand_gen.randint(0, 255) for b in data])

def gen_s():
    current_time = int(time.time())
    seed = (current_time>>3)<<3
    return seed

def recvall(sock, n):
    data = b''
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data

# --- Serveur ---
def start_server(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', port))
    server.listen()
    print(f"Serveur démarré sur le port {port}. En attente de connexions...")

    clients = []
    clients_lock = threading.Lock()

    def handle_client(client_socket, address):
        print(f"Nouvelle connexion de {address}")

        # Générer le seed basé sur le timestamp actuel
        seed = gen_s()
        rand_gen = random.Random(seed)

        with clients_lock:
            clients.append((client_socket, rand_gen))

        while True:
            try:
                # Recevoir la taille du message (4 octets)
                raw_msglen = recvall(client_socket, 4)
                if not raw_msglen:
                    break
                msglen = struct.unpack('!I', raw_msglen)[0]
                # Recevoir le message chiffré
                encrypted_msg = recvall(client_socket, msglen)
                if not encrypted_msg:
                    break
                # Déchiffrer le message
                message = c(encrypted_msg, rand_gen).decode('utf-8', errors='ignore')
                print(f"{address} : {message}")
                broadcast(f"{address} : {message}", client_socket)
            except Exception as e:
                print(f"Erreur avec {address}: {e}")
                break

        print(f"Connexion fermée de {address}")
        with clients_lock:
            clients.remove((client_socket, rand_gen))
        client_socket.close()

    def broadcast(message, sender_socket):
        with clients_lock:
            for client, rand_gen in clients:
                if client != sender_socket:
                    try:
                        encrypted_msg = c(message.encode('utf-8'), rand_gen)
                        client.sendall(struct.pack('!I', len(encrypted_msg)) + encrypted_msg)
                    except:
                        client.close()
                        clients.remove((client, rand_gen))

    def send_server_messages():
        while True:
            try:
                msg = input()
                if msg.lower() == 'exit':
                    print("Arrêt du serveur...")
                    with clients_lock:
                        for client, rand in clients:
                            try:
                                farewell = "Serveur : Arrêt du serveur."
                                encrypted_msg = c(farewell.encode('utf-8'), rand)
                                client.sendall(struct.pack('!I', len(encrypted_msg)) + encrypted_msg)
                                client.close()
                            except:
                                pass
                    server.close()
                    sys.exit()
                if msg.strip() != '':
                    broadcast(msg, None)
            except Exception as e:
                print(f"Erreur d'envoi: {e}")
                break

    send_thread = threading.Thread(target=send_server_messages, daemon=True)
    send_thread.start()

    try:
        while True:
            client_socket, addr = server.accept()
            client_thread = threading.Thread(target=handle_client, args=(client_socket, addr), daemon=True)
            client_thread.start()
    except KeyboardInterrupt:
        print("\nArrêt du serveur par l'utilisateur.")
        with clients_lock:
            for client, rand in clients:
                try:
                    farewell = "Serveur : Arrêt du serveur."
                    encrypted_msg = c(farewell.encode('utf-8'), rand)
                    client.sendall(struct.pack('!I', len(encrypted_msg)) + encrypted_msg)
                    client.close()
                except:
                    pass
        server.close()
        sys.exit()

# --- Client ---
def start_client(host, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((host, port))
    except Exception as e:
        print(f"Impossible de se connecter au serveur : {e}")
        sys.exit(1)
    print(f"Connecté au serveur {host}:{port}")

    # Générer le seed basé sur le timestamp actuel
    seed = gen_s()
    rand_gen = random.Random(seed)

    def receive_messages():
        while True:
            try:
                # Recevoir la taille du message (4 octets)
                raw_msglen = recvall(client, 4)
                if not raw_msglen:
                    print("Déconnecté du serveur.")
                    break
                msglen = struct.unpack('!I', raw_msglen)[0]
                # Recevoir le message chiffré
                encrypted_msg = recvall(client, msglen)
                if not encrypted_msg:
                    print("Déconnecté du serveur.")
                    break
                # Déchiffrer le message
                message = c(encrypted_msg, rand_gen).decode('utf-8', errors='ignore')
                print(f"\r{message}\n> ", end='')
            except Exception as e:
                print(f"\nErreur de réception: {e}")
                break
        client.close()
        sys.exit()

    receive_thread = threading.Thread(target=receive_messages, daemon=True)
    receive_thread.start()

    while True:
        try:
            msg = input("> ")
            if msg.lower() == 'exit':
                farewell = "Client a quitté le chat."
                encrypted_msg = c(farewell.encode('utf-8'), rand_gen)
                client.sendall(struct.pack('!I', len(encrypted_msg)) + encrypted_msg)
                print("Déconnexion...")
                client.close()
                sys.exit()
            if msg.strip() != '':
                encrypted_msg = c(msg.encode('utf-8'), rand_gen)
                client.sendall(struct.pack('!I', len(encrypted_msg)) + encrypted_msg)
        except KeyboardInterrupt:
            farewell = "Client a quitté le chat."
            encrypted_msg = c(farewell.encode('utf-8'), rand_gen)
            try:
                client.sendall(struct.pack('!I', len(encrypted_msg)) + encrypted_msg)
            except:
                pass
            print("\nDéconnexion...")
            client.close()
            sys.exit()
        except Exception as e:
            print(f"Erreur d'envoi: {e}")
            break

# --- Main ---
if __name__ == "__main__":
    if len(sys.argv) < 3:
        usage()

    mode = sys.argv[1].lower()

    if mode == "serveur":
        if len(sys.argv) != 3:
            usage()
        try:
            port = int(sys.argv[2])
        except ValueError:
            print("Le port doit être un entier.")
            sys.exit(1)
        start_server(port)
    elif mode == "client":
        if len(sys.argv) != 4:
            usage()
        host = sys.argv[2]
        try:
            port = int(sys.argv[3])
        except ValueError:
            print("Le port doit être un entier.")
            sys.exit(1)
        start_client(host, port)
    else:
        usage()
