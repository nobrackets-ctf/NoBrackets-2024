from pyModbusTCP.client import ModbusClient
from time import sleep

c = ModbusClient(host="localhost", port=502, unit_id=1, auto_open=True)

def get_entry():
    return c.read_discrete_inputs(1, 1)[0]

def get_transfer(n):
    return c.read_discrete_inputs(4-n, 1)[0]

def get_exit():
    return c.read_discrete_inputs(4, 1)[0]

def start_entry_conveyor():
    c.write_single_coil(5, 1)

def stop_entry_conveyor():
    c.write_single_coil(5, 0)

def start_exit_conveyor():
    c.write_single_coil(0, 1)

def stop_exit_conveyor():
    c.write_single_coil(0, 0)

def load(n):
    if n == 2: base = 1
    else : base = 6
    c.write_single_coil(base, 1)
    c.write_single_coil(base+1, 0)
    c.write_single_coil(base+2, 0)
    c.write_single_coil(base+3, 0)

def unload(n):
    if n == 2: base = 1
    else : base = 6
    c.write_single_coil(base, 0)
    c.write_single_coil(base+1, 1)
    c.write_single_coil(base+2, 0)
    c.write_single_coil(base+3, 0)

def transfer_right(n):
    if n == 2: base = 1
    else : base = 6
    c.write_single_coil(base, 0)
    c.write_single_coil(base+1, 0)
    c.write_single_coil(base+2, 1)
    c.write_single_coil(base+3, 0)

def transfer_left(n):
    if n == 2: base = 1
    else : base = 6
    c.write_single_coil(base, 0)
    c.write_single_coil(base+1, 0)
    c.write_single_coil(base+2, 0)
    c.write_single_coil(base+3, 1)

def transfer_reset(n):
    if n == 2: base = 1
    else : base = 6
    c.write_single_coil(base, 0)
    c.write_single_coil(base+1, 0)
    c.write_single_coil(base+2, 0)
    c.write_single_coil(base+3, 0)

start_exit_conveyor()
while True:
    start_entry_conveyor()
    load(1)
    while not get_transfer(1):
        sleep(0.1)
    stop_entry_conveyor()
    transfer_left(1)
    transfer_left(2)
    while not get_transfer(2):
        sleep(0.1)
    load(2)
    while get_exit():
        sleep(0.1)
