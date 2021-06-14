import pyautogui
import os
import time
import tkinter
from tkinter import messagebox


def get_current_position():
    current_path = os.getcwd()
    return current_path


def get_settings():
    try:
        with open(get_current_position() + "\MouseSettings.txt") as config:
            for line in config:
                if "time" in line:
                    time_set = line.strip(" ").split("=")[1]
                    return int(time_set)

    except FileNotFoundError:
        message = "The MouseSettings.txt file has to be in the same directory as the executable!"
        message_box(message)
        exit()


def message_box(message):
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showerror(title="Error", message=message)


def mouse_movement():
    pyautogui.move(1, 0)
    pyautogui.move(-1, 0)
    pyautogui.move(0, 1)
    pyautogui.move(0, -1)


if __name__ == "__main__":
    while True:
        mouse_movement()
        time.sleep(15)

