import subprocess
import time
import sys
import os
import signal
import psutil
import threading
import tkinter as tk
from tkinter import messagebox

session_id = '2'
checkEvery = 10 # Time in seconds

#Check if trex is running
def check_trex_running():
    status = os.system('systemctl is-active --quiet trex')
    if (status):
        return False
    else:
        return True

#Check if the user account is locked - Change the argument of '2' below to match your session ID 
def isAccountLocked():
    accStatus = subprocess.run("loginctl show-session -p LockedHint" + session_id,capture_output=True,shell=True).stdout.decode("utf-8").strip()
    if accStatus == "LockedHint=no":
       return False
    elif accStatus == "LockedHint=yes":
        return True
    else: # Go ahead and start TREX if there is an issue checking if locked
        return True

#Every 10 minutes check if the process is still running and If our check function returns false, ask the user if they would like to start it. If no input is recieved start the systemctl service.
def main():
    while True:
        time.sleep(checkEvery)
        if check_trex_running() == False and isAccountLocked() == False:
            root = tk.Tk()
            root.withdraw()
            MsgBox = messagebox.askquestion("Trex Not Running", "Trex is not running. Would you like to start it?")
            if MsgBox == 'yes':
                root.destroy()
                subprocess.call(['systemctl', 'start', 'trex'])
            else:
                root.destroy()
        elif check_trex_running() == False and isAccountLocked() == True:
            print("Starting TREX silently")
            subprocess.call(['systemctl', 'start', 'trex'])
        else:
            print("Trex should be running!")

#Start the thread that checks trex every 10 minutes
threading.Thread(target=main).start()
