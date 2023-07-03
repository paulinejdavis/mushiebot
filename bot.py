import webbrowser
import time
import pyautogui

for i in range (10):
    webbrowser.open('https://www.imdb.com/name/nm0631217/?ref_=ttfc_fc_cr24')
    time.sleep(5)
    x=600
    y=600
    pyautogui.moveTo(x, y, duration=10)

    pyautogui.scroll(-1000)

    x=1341
    y=12
    pyautogui.moveTo(x, y, duration=10)
    pyautogui.click()

  