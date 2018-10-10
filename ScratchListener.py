# This program listens for Scratch broadcasts, to enable the SMARS robot to be controlled via Scratch.
# Code from https://en.scratch-wiki.info/wiki/Communicating_to_Scratch_via_Python_with_a_GUI


from array import array
import socket
import time
import sys

from Tkinter import Tk
from tkSimpleDialog import askstring
root = Tk()
root.withdraw()

PORT = 42001
HOST = askstring('Scratch Connector', 'IP:')
if not HOST:
    sys.exit()

print("Connecting...")
scratchSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
scratchSock.connect((HOST, PORT))
print("Connected!")

def sendScratchCommand(cmd):
    n = len(cmd)
    a = array('c')
    a.append(chr((n >> 24) & 0xFF))
    a.append(chr((n >> 16) & 0xFF))
    a.append(chr((n >>  8) & 0xFF))
    a.append(chr(n & 0xFF))
    scratchSock.send(a.tostring() + cmd)

while True:
    msg = askstring('SMARS to Scratch Connector', 'Send Broadcast:')

    #need to add SMARS commands here.
    if msg:
        sendScratchCommand('broadcast "' + msg + '"')
