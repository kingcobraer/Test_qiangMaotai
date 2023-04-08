import pyautogui

aa = pyautogui.locateOnScreen('busy.png', confidence=0.8, grayscale=True)

print(pyautogui.position())

print(aa)

# Box(left=249, top=673, width=412, height=51)
#
#

