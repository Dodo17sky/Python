import threading
import serial
import msvcrt, sys
from datetime import datetime

connected = False
port = 'COM4'
bauds = [ 9600, 57600, 115200 ]

data = ""

def print_info_ascii(msg):
    for c in msg:
        if c == "\n":
            print ord("\n"), "-", "\\n"
        elif c == "\r":
            print ord("\n"), "-", "\\r"
        elif c == "\0":
            print ord("\n"), "-", "\\0"
        else:
            print ord(c), "-", c

def handle_data(data):
    if data:
        print data,

def read_from_port(ser):
    global connected
    global data
    while not connected:
        #serin = ser.read()
        connected = True

        while True:
            byte = ser.read(1)
            data += byte;
            if byte == "\n":
                # print_info_ascii(data)
                ts = datetime.now().strftime('%H:%M:%S.%f')[:-3]
                print ts + ": " + data,
                data = ""
            if msvcrt.kbhit() and msvcrt.getch() == chr(27).encode():
                sys.exit(0)
            if msvcrt.kbhit():
                if ord(msvcrt.getch()) == 27:
                    break

print " Select baud rate: "
print "  1: 9600"
print "  2: 57600"
print "  3: 115200"
print ""

br = int(raw_input(" Select: "))
baud = bauds[br-1]

serial_port = serial.Serial(port, baud, timeout=0)

thread = threading.Thread(target=read_from_port, args=(serial_port,))
thread.start()