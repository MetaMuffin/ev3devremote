import socket
from time import sleep

host = "0.0.0.0" 
port = 0
secret = "" # not actually secret because the socket is not encrypted
client_socket = None
loggging = False

def do_logging():
    loggging = True

def config_device(host_,port_,secret_):
    host = host_
    port = port_
    secret = secret_

    client_socket = socket.socket() # establish a socket connection 
    client_socket.connect((host, port))

    if sock_send("auth {}".format(secret.replace(" ","-"))) == "ok":
        return "ok"
    else:
        raise Exception("Authentification Failed. Secret might not be correct.")

def sock_send(msg):
    if loggging: print('[o] ' + msg)
    client_socket.send(msg.encode())
    data = client_socket.recv(1024).decode()
    if loggging: print('[i] ' + data) 
    return data

def config_tank_drive(ports):
    return sock_send("cfg_tank_drive {}".format(ports))

def config_port(port,type_):
    return sock_send("cfg_port {} {}".format(port,type_))

def config_mode(port,mode):
    return sock_send("cfg_mode {} {}".format(port,mode))

def motor(port,speed):
    return sock_send("motor {} {}".format(port,str(int(speed))))

def tank_drive(ports,speed_a,speed_b):
    return sock_send("tank_drive {} {} {}".format(ports,str(int(speed_a)),str(int(speed_b))))

def value(port):
    res = sock_send("value {}".format(port))
    if not res.startswith("err"):
        return float(res)
    else:
        raise Exception("Device not connected or configured.")