import __init__ as e3r
from time import sleep

e3r.config_device("192.168.0.2",5000,"wub-wub-wub")
e3r.config_tank_drive("AB")
e3r.config_port("4","us")
e3r.config_mode("4","US-DIST-CM")

e3r.tank_drive("AB",20,20)
sleep(1)
e3r.tank_drive("AB",0,0)
e3r.value("1")

