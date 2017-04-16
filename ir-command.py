#!/usr/bin/env python
import sys, time
#sys.path.append('/storage/.kodi/addons/script.module.pyserial/pyserial')
import serial

port = "/dev/uarduino"

#TV off: 4004:100FCFD
#TV on 4004:1007C7D
#Spkr Off: 1EE1FE01
#Spkr on: 1EE17E81
#Clear voice off: 7E8141BE
#Clear voice on: 7E8101FE
#BT src: 1EE1946B

commands={
'on': [
    "1EE17E81", #Spk on
    "4004:1007C7D", #TV on
    "1EE152AD", #BDsrc
    "1EE19B64", #Movie
    "7E8101FE" ], #Clear Voice on
'off': [
    "4004:100FCFD", #TV off
    "1EE10AF5", #Stereo
    "7E8141BE", #Clear Voice off
    "1EE1FE01" ], #Spk off
'volup': ["1EE17887"],
'voldown': ["1EE1F807"]
}

ser = serial.Serial(
    port=port,\
    baudrate=115200,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
    timeout=5)

def read_line():
    for c in ser.read():
        #print(c)
        if c == '\n':
            break

def send(cmd):
    #print(cmd)
    ser.write(cmd+'\n')

def action(commands):
    for cmd in commands:
        send(cmd)
        #print(ser.readline())
        time.sleep(0.5)

act = sys.argv[1].lower()
action(commands[act])

ser.close()

