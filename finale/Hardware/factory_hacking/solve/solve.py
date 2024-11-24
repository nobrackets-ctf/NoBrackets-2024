from pyModbusTCP.client import ModbusClient
from time import sleep

c = ModbusClient(host="localhost", port=502, unit_id=1, auto_open=True)

def start():
    for _ in range(20):
        c.write_single_coil(5, 1) # conveyor
        c.write_single_coil(6, 0) # load
        c.write_single_coil(7, 0) # unload
        c.write_single_coil(8, 0) # transfer right
        c.write_single_coil(9, 0) # transfer left
        c.write_single_coil(6, 1) # load
        sleep(0.01)

def place():
    for _ in range(20):
        c.write_single_coil(5, 0) # conveyor
        c.write_single_coil(8, 1) # transfer right
        sleep(0.01)
    sleep(10)
    for _ in range(20):
        c.write_single_coil(8, 0) # transfer right
        c.write_single_coil(9, 1) # transfer left

while True:
    start()
    while c.read_discrete_inputs(3, 1) == [0]: # At transfer 1
        sleep(0.1)
    place()