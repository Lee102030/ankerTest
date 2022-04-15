from tkinter import filedialog
from pythonping import *
from colorama import Fore, Style
import socket
import time
import os
import shutil

def setDpiAwareness():
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass


def uploadFilebuttonPressed(objIPListFromMain):
    badIPList = []
    counterBadIPList = 0
    print("uploadFilebuttonPressed")
    ipListToPing = []
    try:
        filePath = filedialog.askopenfilename()
        rawFile = open(filePath, "rt")
        print(f"{filePath} loaded. \n")
        for i in rawFile:
            ipListToPing.append(i.replace("\n", ""))
        if len(ipListToPing) == 0:
            raise FileNotFoundError
        for j in ipListToPing:
            returnFromPing = pingDevicesAndReturnBool(j)
            if not returnFromPing:
                badIPList.append(j)
                counterBadIPList += 1
        if counterBadIPList > 0:
            print(Fore.RED + f"{badIPList}")
            print(Style.RESET_ALL, end="")
            raise Exception
        else:
            objIPListFromMain.listValidIP = ipListToPing
            objIPListFromMain.flag = "active"
    except FileNotFoundError:
        print("File empty or path invalid.")
        objIPListFromMain.flag = "disabled"
    except Exception:
        print(f"{counterBadIPList} Device(s) not responsive found")
        objIPListFromMain.flag = "disabled"


def loadHexaButtonPressed():
    print("loadHexaButtonPressed")

def pingDevicesAndReturnBool(IPListFromRawFile):
    return ping(IPListFromRawFile).success()

def retrieveFirmwareVersionFX(ipTocheckFirmwareVersion):
    try:
        s = socket.socket()
        HOST = ipTocheckFirmwareVersion
        PORT = 10001
        s.connect((HOST,PORT))
        echo = s.recv(1024)
        time.sleep(1)
        if str(echo)[2:12] == "<s>ECHO<e>":
            s.send(b'version\r\n')
            firmwareVersion = s.recv(1024)
            s.close()
            return str(firmwareVersion)[2:]
    except Exception:
        print("error exception")
    except ConnectionError:
        print("connectionError")

def fileSystemPreparation(objFromMain):
    print("filesys")
    print(objFromMain.listValidIP)
    try:
        if os.path.exists("c:/tempVSPE"):
            shutil.rmtree("c:/tempVSPE")
        os.makedirs("c:/tempVSPE", mode=0o666)
        print("Temporary directory tempVSPE created.\n")
    except OSError:
        print("Error folder creation")

    try:
        rawFileVSPE = open("../config/VSPE.vspe", "rb")
        rawFileContents = rawFileVSPE.read()
        fileVSPEConfigByteArray = bytearray(rawFileContents)
        print(len(fileVSPEConfigByteArray))

        #for i in range(len(fileVSPEConfigByteArray)):
        #    print(f"{i} = {chr(fileVSPEConfigByteArray[i])}")
    except:
        print("file error")
        #

        #fileVSPEConfigByteArray[46] = ord(objFromMain.listValidIP[0][8])
        #VSPEFileToCreate = bytes(fileVSPEConfigByteArray)
        #for i in range(len(objFromMain.listValidIP)):
        #    f1 = open(f"c:/tempVSPE/a.vspe", "wb")
        #    f1.write(VSPEFileToCreate)
        #f1.close()
        #time.sleep(5)

        """
        import os
import shutil

class IPListClass:
    def __init__(self,listValidIP):
        self.listValidIP = listValidIP

objFromMain = IPListClass(["172.16.205.105"])

print(objFromMain.listValidIP)

try:
    if os.path.exists("c:/tempVSPE"):
        shutil.rmtree("c:/tempVSPE")
    os.makedirs("c:/tempVSPE", mode=0o666)
    print("Temporary directory tempVSPE created.\n")
except OSError:
    print("Error folder creation")
try:
    rawFileVSPE = open("VSPE.vspe", "rb")
    rawFileContents = rawFileVSPE.read()
    fileVSPEConfigByteArray = bytearray(rawFileContents)

    for i in range(0,86):
        print(f"{i} = {chr(fileVSPEConfigByteArray[i])}")

    print(chr(fileVSPEConfigByteArray[8]))

    arrayObj = bytearray(len(fileVSPEConfigByteArray))
    arrayObjStart = fileVSPEConfigByteArray[0:38]
    arrayObjMidIP = fileVSPEConfigByteArray[38:52]
    arrayObjFinal = fileVSPEConfigByteArray[52:]

    print(arrayObjMidIP)
    arrayObjMidIP[13] = ord("6")
    finalArray = arrayObjStart + arrayObjMidIP + arrayObjFinal
    print(finalArray)




    test = open("c:/tempVSPE/test.vspe", "ab")
    test.write(finalArray)

    #tempArrayToCarryStartVSPE.close()
except:
    print("file error")
        
        
        for i in range(38,52):
            print(f"{i} = ", end="")
            print(chr(fileVSPEConfigByteArray[i]))
        fileVSPEConfigByteArray[49] = ord(objFromMain.listValidIP[0][11:12])
        fileVSPEConfigByteArray[50] = ord(objFromMain.listValidIP[0][12:13])
        fileVSPEConfigByteArray[51] = ord(objFromMain.listValidIP[0][13:14])
        VSPEFileToCreate = bytes(fileVSPEConfigByteArray)
        for i in range(2):
            f1 = open(f"c:/tempVSPE/{i}.vspe", "wb")
            f1.write(VSPEFileToCreate)
        f1.close()
        #time.sleep(5)
        #shutil.rmtree('c:/tempVSPE')
        """


"""
class IPListClass:
    def __init__(self, listValidIP, flag):
        self.listValidIP = listValidIP
        self.flag = flag

105 mode
    try:
        rawFileVSPE = open("VSPE.vspe", "rb")
        rawFileContents = rawFileVSPE.read()
        fileVSPEConfigByteArray = bytearray(rawFileContents)
        for i in range(38,52):
            print(f"{i} = ", end="")
            print(chr(fileVSPEConfigByteArray[i]))
        fileVSPEConfigByteArray[49] = ord(objFromMain.listValidIP[0][11:12])
        fileVSPEConfigByteArray[50] = ord(objFromMain.listValidIP[0][12:13])
        fileVSPEConfigByteArray[51] = ord(objFromMain.listValidIP[0][13:14])
        VSPEFileToCreate = bytes(fileVSPEConfigByteArray)
        for i in range(2):
            f1 = open(f"c:/tempVSPE/{i}.vspe", "wb")
            f1.write(VSPEFileToCreate)
        f1.close()
        #time.sleep(5)
        #shutil.rmtree('c:/tempVSPE')
    except:
        print("file error")
"""
