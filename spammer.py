import time
import pyautogui

def run():
    print("Starting in 5 seconds...")
    time.sleep(5)
    f = open("beemovie.txt", 'r')
    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
    
if __name__ == '__main__':
    run()
