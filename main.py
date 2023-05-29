import pyautogui
import time
import ctypes
import datetime
import threading
import os

current_folder = os.getcwd()
Donate_Button = os.path.join(current_folder, 'Donate_Button.png')
Quick_Donate_Button = os.path.join(current_folder, 'Quick_Donate.png')
Failsafe = os.path.join(current_folder, 'ilsafe.png')
ScrollDown = os.path.join(current_folder, 'ScrollDown.png')
Anyonethere = os.path.join(current_folder, 'Anyonethere.png')
RecentApps = os.path.join(current_folder, 'ecentapps.png')
ClearAll = os.path.join(current_folder, 'ClearAll.png')
ClashIcon = os.path.join(current_folder, 'ClashIcon.png')
GoBack = os.path.join(current_folder, 'GoBack.png')

TotalDonations = 0
Resetting = False
SecondsToReset = 0
ResetEverySeconds = 600 #15 mins

def resetclash():
    global Resetting
    Resetting = True
    img = pyautogui.locateOnScreen(RecentApps, grayscale=False, confidence=0.7)
    print(gettime() + "Resetting Clash")
    if img is not None:
        x, y, width, height = img
        image_center_x = x + width / 2
        image_center_y = y + height / 2
        pyautogui.click(image_center_x, image_center_y)
        title(gettime() + "Clicking recent apps")
        time.sleep(3)

    pyautogui.click(1300, 120)
    
    time.sleep(3)

    img3 = pyautogui.locateOnScreen(ClashIcon, grayscale=False, confidence=0.6)
    if img3 is not None:
        x, y, width, height = img3
        image_center_x = x + width / 2
        image_center_y = y + height / 2
        pyautogui.click(image_center_x, image_center_y)
        title(gettime() + "Launching Clash of Clans")
        print(gettime() + "Relaunched Clash")
        
    time.sleep(5)
    Resetting = False

def run_resetclash_periodically():
    global SecondsToReset
    global ResetEverySeconds
    global TotalDonations
    SecondsToReset = ResetEverySeconds
    while True:
        for i in range(ResetEverySeconds):
            time.sleep(1)
            SecondsToReset -=1
            title("Waiting for new donations - Total: " + str(TotalDonations) + " - Time To Reset: " + str(SecondsToReset) + " Seconds")

        resetclash()
        SecondsToReset = ResetEverySeconds

def gettime():
    current_time = datetime.datetime.now()
    time_string = "[" + current_time.strftime("%H:%M:%S") + "] "
    return time_string

def title(title):
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleTitleW(title)

def FindGreenPart():
    global TotalDonations
    pyautogui.click(1583, 4335, 1)
    pyautogui.click(1369, 436, 9)

    pyautogui.click(1052, 622, 5)
    pyautogui.click(1165, 624, 5)

    if pyautogui.locateOnScreen(GoBack, grayscale=False, confidence=0.6) is not None:
        pyautogui.click(1162, 428, 5)
        pyautogui.click(1156, 293, 5)
        pyautogui.click(1056, 434, 5)
        pyautogui.click(1033, 285, 5)

    print(gettime() + "Finished donating")
    TotalDonations += 1

def FindQuickDonateButton():
    title("Waiting for quick donations")
    
    pyautogui.click(1162, 428, 5)
    pyautogui.click(1156, 293, 5)
    pyautogui.click(1056, 434, 5)
    pyautogui.click(1033, 285, 5)

    img = pyautogui.locateOnScreen(Quick_Donate_Button, grayscale=False, confidence=0.6)

    if img is not None:
        x, y, width, height = img
        image_center_x = x + width / 2
        image_center_y = y + height / 2
        pyautogui.click(image_center_x, image_center_y)
        title(gettime() + "Found quick donate button")
        time.sleep(1)
        FindGreenPart()

def FindDonateButton():
    global TotalDonations
    global Resetting
    global ResetEverySeconds
    if Resetting == False:
        if pyautogui.locateOnScreen(ClashIcon, grayscale=False, confidence=0.8) is not None:
            resetclash()
        if pyautogui.locateOnScreen(Anyonethere, grayscale=False, confidence=0.8) is not None: 
            print(gettime() + "Reloaded from inactivity")
            pyautogui.click(794, 610)
        if pyautogui.locateOnScreen(Failsafe, grayscale=False, confidence=0.8) is None:
            if pyautogui.locateOnScreen(ScrollDown, grayscale=False, confidence=0.8) is not None:
                pyautogui.click(387, 843)
                print(gettime() + "Scrolled down")
            img = pyautogui.locateOnScreen(Donate_Button, grayscale=False, confidence=0.8)
            if img is not None:
                x, y, width, height = img
                image_center_x = x + width / 2
                image_center_y = y + height / 2
                pyautogui.click(image_center_x, image_center_y)
                title("Found donation button")
                time.sleep(1)
                FindQuickDonateButton()
        else:
            print(gettime() + "Going back to clan chat...")
            pyautogui.click(343,467)
    else:
        title("Currently Resetting")

resetclash_thread = threading.Thread(target=run_resetclash_periodically)
resetclash_thread.start()

while True:
    FindDonateButton()
    time.sleep(2)
