
# ev3devremote

This is a framework for remote conroling the ev3dev device using python on both the ev3 and the host (remote controller).
The host will send packets via sockets to the device, wich will then respond with data or an ackonknowledgement

Each function returns (if nothing else is specified) `"ok"` or an error message.

Function call|Description
-|-|-
`config_tank_drive(`ports`)`|Configurates two motor outputs to be run with only one function call to `tank_drive`. If the requested device is not connected the function returns `"err Requested Device Not Found"`.
`config_port(`port,type`)`|Configurates a port the device. type is a string which is one of the ones listed below. If the requested device is not connected the function returns `"err Requested Device Not Found"`.
`config_mode(`port,mode`)`|Sets the mode of a connected sensor or motor. Modes are listed below
`do_logging()`|Enables logging of each packet sent in the console of the host. This function does not transmit any data to the ev3
`motor(`port,speed`)`|Runs a single motor with a given speed percentage.
`tank_drive(`ports,speed_a,speed_b`)`|Runs two motors on the ports with the given speed_percentage
`value(`port`)`|Get the value of an sensor. returns a float. 

## Motor and Sensor Types

Type string for the functions|Name in the ev3dev2 python module
-|-
`us`|Ultrasonic Sensor
`ir`|Infrared Sensor
`ts`|Touch Sensor
`gy`|Gyro Sensor
`m`|Large Motor

## Modes

The mode of a motor or sensor is the same string that is also used in the ev3de2 python module.

## Ports

The argument for the port is a string.
If more then one port needs to be specified, just concatenate the strings of both individual ports.

Argument|Name
-|-
A | Output A
B | Output B
C | Output C
D | Output D
1 | Input 1
2 | Input 2
3 | Input 3
4 | Input 4

## Refences

If you need to impliment more functionality or want to find out more, visit the website of the [ev3dev python module](https://ev3dev-lang.readthedocs.io/projects/python-ev3dev/en/stable/) and the [ev3dev website](https://www.ev3dev.org/)
