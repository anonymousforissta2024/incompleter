#Source: https://stackoverflow.com/questions/71490260/my-pyautogui-script-is-raising-typeerror-nonetype-object-is-not-subscriptable
while keyboard.is_pressed('q') == False:

    pic = pyautogui.screenshot(region=(360,158,1900,1025))

    width, height = pic.size

    if pyautogui.locateOnScreen('greenlightning.png', region=(360,158,1900,1025), grayscale=True, confidence=0.8) != None:
        lightningloc = pyautogui.locateOnScreen('greenlightning.png')
        x = lightningloc[0]
        y = lightningloc[1]
        pyautogui.click(x, y - 50)
        time.sleep(0.2)
    else:
        time.sleep(0.1)