import pyautogui
import time
import mss
import datetime


def zoom_out(i=17):
    # Number of scroll steps (adjust as needed)
    scroll_steps = i
    
    # Hold Control (simulate by repeatedly pressing)
    for _ in range(scroll_steps):
        pyautogui.keyDown('ctrl')
        pyautogui.scroll(-10)  # Negative value scrolls down
        pyautogui.keyUp('ctrl')
def zoom_in(i=17, k=0):
    if k == 1:
        for _ in range(15):
            pyautogui.keyDown('ctrl')
            pyautogui.scroll(50) 
            pyautogui.keyUp('ctrl')
    else:
        # Number of scroll steps (adjust as needed)
        scroll_steps = i

        # Hold Control (simulate by repeatedly pressing)
        for _ in range(scroll_steps):
            pyautogui.keyDown('ctrl')
            pyautogui.scroll(10)  # Positive value scrolls up
            pyautogui.keyUp('ctrl')


def drag():
    # Starting coordinates (where to click and hold)
    x_start, y_start = 1920//2, 1080//2  # Replace with your desired coordinates

    # Ending coordinates (where to drag to)
    x_end, y_end = 400, 500  # Replace with your desired coordinates

    pyautogui.moveTo(x_start, y_start)
    # Hold down the left mouse button
    pyautogui.mouseDown(button='left')

    # Move the mouse to the end coordinates
    pyautogui.moveTo(x_end, y_end, duration=2)  # Adjust duration as needed

    # Release the left mouse button
    pyautogui.mouseUp(button='left')


def take_screenshot(filename):
    with mss.mss() as sct:
        # Capture the entire screen
        monitor = sct.monitors[1]  # Change index if you have multiple monitors
        sct_img = sct.grab(monitor)

        # Save the screenshot with high quality
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=filename,level=2)  # Adjust the compression level as needed


if __name__ == "__main__":
    out_path = r"C:\Users\omkis\Downloads\MillionLords\Train\Experiments\ScreenShots"
    time.sleep(3)
    zoom_in(k=1)
    time.sleep(0.2)
    zoom_out()
    for i in range(50):
        drag()
        zoom_in(k=1)
        time.sleep(1)
        zoom_out()
        timestamp = str(int(time.time()))  # Generating timestamp
        filename = out_path + f"\screenshot_{timestamp}.png"
        take_screenshot(filename)
        time.sleep(0.2)
        print(f"Screenshot saved as {filename}")
        