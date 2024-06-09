import os
import time
import subprocess
from datetime import datetime
from pynput import mouse, keyboard

IDLE_TIME = 5  # Time in seconds to wait for inactivity
SCREENSHOT_INTERVAL = 10  # Time in seconds between each screenshot
ENCRYPTED_PATH = "/opt/journey/screenshots"  # Replace with your encrypted directory path

def on_activity():
    global last_activity_time
    last_activity_time = time.time()

def take_screenshot():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_path = os.path.join(ENCRYPTED_PATH, f"screenshot_{timestamp}.png")
    subprocess.run(["flameshot", "full", "--path", screenshot_path])
    print(f"Screenshot saved: {screenshot_path}")

def main():
    global last_activity_time
    last_activity_time = time.time()

    mouse_listener = mouse.Listener(on_move=on_activity, on_click=on_activity, on_scroll=on_activity)
    mouse_listener.start()

    keyboard_listener = keyboard.Listener(on_press=on_activity, on_release=on_activity)
    keyboard_listener.start()

    while True:
        if time.time() - last_activity_time > IDLE_TIME:
            take_screenshot()
            time.sleep(SCREENSHOT_INTERVAL)
        else:
            time.sleep(1)

if __name__ == "__main__":
    main()