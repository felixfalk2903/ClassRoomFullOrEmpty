import serial

ser = serial.Serial('/dev/ttyACM1', 115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

while True:
    print(ser.readline())