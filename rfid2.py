from time import sleep
import serial

def readRFID():
    ser=serial.Serial("/dev/ttyUSB0")
    ser.baudrate=9600
    data=ser.read(12)
    ser.close()
    return data


while True:
    get_id=readRFID()
    print(get_id)
    if get_id=="21323":
        print("asd")
    else:
        print("asd")

