import time
import serial
def readRfid():
    ser=serial.Serial("/dev/ttyusb0")
    ser.baudrate=9600
    data=ser.read()
    ser.close()
    return data

while True:
    data=readRfid()
    print(data)
    if data=='21313213213213':
        print("Access granted")
    elif data=='dasdasdasd':
        print("Acesss Granted")
    else:
        print("Access Diened")