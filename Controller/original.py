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


sound = Sound()

driver = MoveTank(OUTPUT_A, OUTPUT_B)
us = UltrasonicSensor(INPUT_4)
gs = GyroSensor(INPUT_2)

gs.mode = "GYRO-ANG"
us.mode = "US-DIST-CM"

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
        if a[0]=="motor":
            driver.on(SpeedPercent(int(a[1])),SpeedPercent(int(a[2])))
            data = "ok"
            conn.send(data.encode())
        
        elif a[0]=="val":
            data = str(us.value()) + " " + str(gs.value())
            conn.send(data.encode())
        else:
            data = "Berliner Luft- und Badeparadies "
            conn.send(data.encode())


    conn.close()


if __name__ == '__main__':
    while True:
        server_program()