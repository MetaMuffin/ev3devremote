print("Importing...")
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor, GyroSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
from time import sleep
from threading import Thread
import socket
print("Fertig")

ports = {"A":OUTPUT_A,"B":OUTPUT_B,"C":OUTPUT_C,"D":OUTPUT_D,"1":INPUT_1,"2":INPUT_2,"3":INPUT_3,"4":INPUT_4}

port_cfg = {}

def server_program():
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        
        print(data)
        a = data.split(" ")
        data = "ok"

        if a[0]=="cfg_tank_drive":
            if not (a[1][0] in ports.keys() and a[1][1] in ports.keys()):
                data = "err Port unknown"
            else:
                p1,p2 = ports[a[1][0]],ports[a[1][1]]
                port_cfg[a[1]] = MoveTank(p1,p2)

        elif a[0]=="cfg_port":
            if not a[1] in ports.keys():
                data = "err Port unknown"
            else:
                p = ports(a[1])
                o = None
                if a[2] == "m":
                    o = LargeMotor(p)
                elif a[2]=="us":
                    o = UltrasonicSensor(p)
                elif a[2]=="gy":
                    o = GyroSensor(p)

                if o==None:
                    data = "err Type unknown"
                else:
                    port_cfg[a[1]] == o

        elif a[0]=="tank_drive":
            if not a[1] in port_cfg.keys():
                data = "err Port unknown or not configured yet"
            else:
                d = port_cfg[a[1]]
                speed1 = 0
                speed2 = 0
                try:
                    speed1 = int(a[2])
                    speed2 = int(a[3])
                except:
                    data = "err Speed not an int"
                d.on(SpeedPercent(speed1),SpeedPercent(speed2))
            

        elif a[0]=="motor":
            if not a[1] in port_cfg.keys():
                data = "err Port unknown or not configured yet"
            else:
                d = port_cfg[a[1]]
                speed = 0
                try:
                    speed = int(a[2])
                except:
                    data = "err Speed not an int"
                d.on(SpeedPercent(speed))
        
        elif a[0]=="value":
            data = ""
            for pr in a[1]
                if not pr in port_cfg.keys():
                    data = "err Port unknown or not configured yet"
                else:
                    d = port_cfg[a[1]]
                    data = str(d.value()) + " "
            
            data.strip(" ")


        else:
            data = "err Protocol syntax wrong"



        conn.send(data.encode())

    conn.close()


if __name__ == '__main__':
    while True:
        server_program()