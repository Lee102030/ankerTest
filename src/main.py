from tkinter import *
from functions import *
from firmwareUpgradeMainFunction import *

setDpiAwareness()

class IPListClass:
    def __init__(self, listValidIP, flag):
        self.listValidIP = listValidIP
        self.flag = flag




ipListObject = IPListClass([], "disabled")

def uploadFilebuttonPressedBridge():
    uploadFilebuttonPressed(ipListObject)
    if ipListObject.flag == "active":
        counterGoodIP = 0
        print("Sending ICMP Packets / retrieving data from Anker.\n")
        for i in ipListObject.listValidIP:
            print(f'PING sent to Anker {i} / '
                  f'Firmware version: {retrieveFirmwareVersionFX(i)} / STATUS: OK')
            counterGoodIP += 1
        print(f"{counterGoodIP} Device(s) checked and ready to flash.")
        runFirmwareUpgradeButton["state"] = "active"
    else:
        runFirmwareUpgradeButton["state"] = "disabled"
        ipListObject.listValidIP = []

def firmwareUpgradeMainFunctionBridge():
    firmwareUpgradeMainFunction(ipListObject)
    runFirmwareUpgradeButton["state"] = "disabled"


root = Tk()
root.geometry('300x300')
root.resizable(False,False)
root['background']='#2a71b2'             #'#E8E1EE'
root.title('Solcon Anker Firmware Upgrade v1.0')
#solconIcon = PhotoImage(file = 'solconicon.png')
#root.iconphoto(False, solconIcon)

#Upload File Button
uploadFileButton = Button(
    root,
    text='Upload File',
    command=uploadFilebuttonPressedBridge
)
uploadFileButton.place(
    height=30,
    width=70,
    x=20,
    y=20
)

#Upload Hexa
uploadHexaButton = Button(
    root,
    text='Upload .HEX File',
    command=loadHexaButtonPressed
)
uploadHexaButton.place(
    height=30,
    width=150,
    x=20,
    y=60
)

#Run Firmware Button
runFirmwareUpgradeButton = Button(
    root,
    text='Run Firmware Upgrade',
    state="disabled",
    command=firmwareUpgradeMainFunctionBridge
)
runFirmwareUpgradeButton.place(
    height=30,
    width=150,
    x=70,
    y=250
)

#Exit
exitButton = Button(
    root,
    text="Exit",
    command=root.destroy
)
exitButton.place(
    height=30,
    width=50,
    x=230,
    y=250
)

root.mainloop()