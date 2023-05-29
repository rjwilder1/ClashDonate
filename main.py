import pyautogui
import time
import ctypes
import datetime
import threading
import os
import pytesseract
import subprocess
import pygetwindow

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
ResetEverySeconds = 600 #10 mins
Uptime = 0

FullResetEverySeconds = 3600
SecondsToFullReset = 0

def ReadChat(txt):
    left = 355
    top = 780
    width = 920 - left
    height = 860 - top
    screen_image = pyautogui.screenshot()
    target_image = screen_image.crop((left, top, left + width, top + height))
    text = pytesseract.image_to_string(target_image)
    if (txt in text):
        if ('Leader' in text) or ('leader' in text):
            return True
        else:
            return False

def ReadGems():
    left = 1700
    top = 370
    width = 1795 - left
    height = 400 - top
    screen_image = pyautogui.screenshot()
    target_image = screen_image.crop((left, top, left + width, top + height))
    text = pytesseract.image_to_string(target_image)
    clean_text = text.strip()
    return clean_text

def SendChat(txt):
    pyautogui.click(870, 930)
    time.sleep(3)
    pyautogui.typewrite(txt)
    time.sleep(0.5)
    pyautogui.press('enter')

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
    global Uptime
    SecondsToReset = ResetEverySeconds
    while True:
        for i in range(ResetEverySeconds):
            time.sleep(1)
            Uptime +=1
            SecondsToReset -=1
            title("Waiting for new donations - Total: " + str(TotalDonations) + " - Time To Reset: " + str(SecondsToReset) + " Seconds")
        resetclash()
        SecondsToReset = ResetEverySeconds

def FullResetClash():
    global SecondsToFullReset
    global FullResetEverySeconds
    SecondsToFullReset = FullResetEverySeconds
    while True:
        for i in range(FullResetEverySeconds):
            time.sleep(1)
            SecondsToFullReset -=1
        ResetBlueStacks()
        SecondsToFullReset = FullResetEverySeconds

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

def ResetBlueStacks():
    Resetting = True
    subprocess.call(["taskkill", "/F", "/IM", "HD-Player.exe"])
    time.sleep(2)

    subprocess.Popen("C:\Program Files\BlueStacks_nxt\HD-Player.exe")
    time.sleep(4)
    window = pygetwindow.getWindowsWithTitle("BlueStacks App Player")[0]
    window.activate()
    window.resizeTo(244, 152)
    hwnd = window._hWnd
    ctypes.windll.user32.SetWindowPos(hwnd, 0, 0, 0, 0, 0, 0x0001)
    time.sleep(1)
    pyautogui.click(161, 16)

    time.sleep(5)
    resetclash()

def FindDonateButton():
    global TotalDonations
    global Resetting
    global ResetEverySeconds
    global Uptime
    global SecondsToReset
    global SecondsToFullReset
    if Resetting == False:
        if ReadChat("Uptime"):
            SendChat("Total uptime: " + str(Uptime) + " seconds")

        if ReadChat("Donations"):
            SendChat("Total donations: " + str(TotalDonations))

        if ReadChat("Gems"):
            SendChat("Total gems left: " + ReadGems())

        if ReadChat("Soft Reset Time"):
            SendChat("Resetting in " + str(SecondsToReset) + " seconds")

        if ReadChat("Reset Clash"):
            SendChat("Resetting Clash of Clans")
            resetclash()

        if ReadChat("Full Reset Time"):
            SendChat("Full Reset is in " + str(SecondsToFullReset) + " seconds")

        if ReadChat("Hard Reset"):
            SendChat("Completely resetting")
            ResetBlueStacks()

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

resetclash_threadF = threading.Thread(target=FullResetClash)
resetclash_threadF.start()

while True: 
    #pyautogui.displayMousePosition() #(1700, 370) (1795, 400)
    FindDonateButton()
    time.sleep(2)
