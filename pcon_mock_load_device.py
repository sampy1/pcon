"""
PCON Hardware Emulation (Power CONtroller Hardware Emulation)

"""
import sys
import socket
import random


def banner(text, ch='-', length=78):
    """ """
    spaced_text = ' %s ' % text
    banner = spaced_text.center(length, ch)
    return banner

def generate_hardware_values():
    voltage = random.randint(120*.95, 120*1.05)
    current = random.randint(0, 48)
    temperature = random.randint(-20, 110)
    return voltage, current, temperature

def server_program(port=5000):
    # get the hostname
    host = socket.gethostname()
    print(banner(f"Starting Server {host}::{port}"))

    socket_server = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    socket_server.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    socket_server.listen(2)
    
    conn, address = socket_server.accept()  # accept new connection
    print("Connection from: " + str(address))
        
    while True:

        
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        voltage, current, temperature = generate_hardware_values()
        if not data: break            # if data is not received break
        
        print(f"from connected user: {str(data)}")
        
        if   str(data) == "get_load_voltage": data = [str(voltage), "V"]
        elif str(data) == "get_load_current": data = [str(current), "A"]
        elif str(data) == "get_line_voltage": data = [str(voltage), "V"]
        elif str(data) == "get_line_current": data = [str(current), "A"]
        elif str(data) == "shutdown": break
        else: data = str(data) + " not supported"
        
        print(f"returning {data}")
        
        conn.send(str(data).encode())  # send data to the client

    conn.close()  # close the connection

class pcon_hardware_emulator():
    """ """
    def __init__(self, port):
        server_program(port)
    
def test_generate_hardware_values():
    for iteration in range(0, 20):
        voltage, current, temperature = generate_hardware_values()
        print(iteration, voltage, current, temperature)

if __name__ == '__main__':
    print (sys.argv)
    PHE = pcon_hardware_emulator(5500)
    #test_generate_hardware_values()
    
    
# https://stackoverflow.com/questions/10810249/python-socket-multiple-clients