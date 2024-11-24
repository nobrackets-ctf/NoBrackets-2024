from flask import Flask, request, jsonify
from pyModbusTCP.client import ModbusClient

c = ModbusClient(host="localhost", port=502, unit_id=1, auto_open=True)

app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/index.html', methods=['GET'])
def index():
    return app.send_static_file('index.html')

@app.route('/documentation.html', methods=['GET'])
def documentation():
    return app.send_static_file('documentation.html')

@app.route('/images/<path:path>', methods=['GET'])
def send_images(path):
    return app.send_static_file('images/' + path)

@app.route('/favicon.ico', methods=['GET'])
def favicon():
    return app.send_static_file('favicon.ico')

@app.route('/get-flag', methods=['GET'])
def get_flag():
    if c.read_discrete_inputs(0, 1)[0]:
        return jsonify({'message': 'Bien joué ! Voici le flag : NBCTF{Y0u_4r3_an_1ndustri4l_h4ck3r}'})
    else:
        return jsonify({'message': 'Erreur : le capteur ne détecte pas de colis tombé.'})

app.run(host='0.0.0.0', port=80)

