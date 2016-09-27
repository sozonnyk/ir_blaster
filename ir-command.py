#!/usr/bin/env python
import sys, time
#sys.path.append('/storage/.kodi/addons/script.module.pyserial/pyserial')
import serial

port = "/dev/uarduino"

commands = { 
'on': [
    "1EE133CC",  #Spk on
    "4004:100BCBD", #TV on 
    "1EE152AD",  #BD src
    "1EE19B64",  #Movie
    "1EE13AC5" ], #Clear Voice
'off': [
    "4004:100BCBD", #TV off 
    "1EE10AF5",  #Stereo
    "1EE13AC5",  #Clear Voice
    "1EE133CC"], #Spk off
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

