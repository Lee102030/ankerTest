import socket
import time
import subprocess
from subprocess import Popen
from functions import *
import pyautogui as p


def firmwareUpgradeMainFunction(objectFromMain):
    try:
        fileSystemPreparation(objectFromMain)
    except:
        print("fileSystemerror")
    print("\n\nUpgrading Flash.\n\n")
"""
    try:
        print("\n\nUpgrading Flash.\n\n")
        vspeProcess = Popen('C:\\Program Files (x86)\\Eterlogic.com\\'
                                'Virtual Serial Ports Emulator\\'
                                'VSPEmulator.exe -minimize -hide_splash '
                                'c:\\tempVSPE\\a.vspe')
        print(vspeProcess)
        time.sleep(0.2)
        p.press("right")
        p.press("enter")
        time.sleep(5)
        avrospProcess = subprocess.call("C:\\Firmware\\AVROSP -cCOM6 -dATxmega256A3 -ifV1.7_JH-inklBootloader.hex -pf -vf")
        print(avrospProcess)

        #print("delete temp")
        #time.sleep(2)
        #shutil.rmtree('c:/tempVSPE')
    except Exception:
        print("error exception")
    except ConnectionError:
        print("connectionError")

    for i in objectFromMain.listValidIP:
    s = socket.socket()
    HOST = i
    PORT = 10001
    s.connect((HOST, PORT))
    echo = s.recv(1024)
    time.sleep(1)
    print(f"{str(echo)[2:12]} from device {i} received")
    time.sleep(1)
    print("Sending 'bootloader' command.")
    s.send(b'bootloader\r\n')
    time.sleep(2)
    print(f"{str(s.recv(1024))[2:24]} received")
    time.sleep(2)
    s.send(b'E\r\n')
    time.sleep(2)
    print("done")
    s.close()


objectFromMain.flag = "disabled"

   result = []
    win_cmd = 'ipconfig'
    process = subprocess.Popen(win_cmd,
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    for line in process.stdout:
        print(line)
    result.append(line)
    errcode = process.returncode
    for line in result:
        print(line)
"""