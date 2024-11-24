import os
import zipfile
import io
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt_and_unzip(encrypted_file_path, aes_key_hex, iv_hex):
    # Convert the AES key and IV from hex to bytes
    aes_key = bytes.fromhex(aes_key_hex)
    iv = bytes.fromhex(iv_hex)

    # Ensure the key and IV lengths are correct
    assert len(aes_key) == 32, f"AES key length is {len(aes_key)}, expected 32 bytes."
    assert len(iv) == 16, f"IV length is {len(iv)}, expected 16 bytes."

    # Read the encrypted data from the file
    with open(encrypted_file_path, 'rb') as f:
        encrypted_data = f.read()

    # Initialize AES cipher for decryption using the key and IV
    cipher = AES.new(aes_key, AES.MODE_CBC, iv)

    try:
        # Decrypt the data
        decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

        # Use BytesIO to handle the decrypted zip data
        zip_buffer = io.BytesIO(decrypted_data)
        
        # Extract the zip file contents
        extraction_dir = 'extracted_contents'
        os.makedirs(extraction_dir, exist_ok=True)
        with zipfile.ZipFile(zip_buffer, 'r') as zip_ref:
            zip_ref.extractall(extraction_dir)

        return extraction_dir
    except ValueError as e:
        print(f"Error during decryption: {e}")
        return None

# Example usage:
if __name__ == "__main__":
    # Example path to the encrypted file
    encrypted_file_path = 'received_exfiltration.zip'  # Replace with actual path to the encrypted file
    
    # AES key and IV provided (replace with actual values)
    aes_key_hex = "a6bbd18198e6ffdafb5b27d6b71f1d4161802900420124296bdf08f7a3aa8705"
    iv_hex = "5757674f767a495348574f51356e567a"

    # Decrypt and unzip the received data
    extracted_dir = decrypt_and_unzip(encrypted_file_path, aes_key_hex, iv_hex)

    if extracted_dir:
        print(f"Files extracted to: {extracted_dir}")
    else:
        print("Decryption failed.")
