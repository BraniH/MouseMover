import pyautogui
import os
import time


def get_current_position():
    current_path = os.getcwd()
    return current_path


def get_settings():
    with open(get_current_position() + "\MoveSettings.txt") as config:
        for line in config:
            if "time" in line:
                time_set = line.strip(" ").split("=")[1]
                return int(time_set)


def mouse_movement():
    pyautogui.dragRel(1, 0, duration=0)


if __name__ == "__main__":
    while True:
        mouse_movement()
        time.sleep(get_settings())
