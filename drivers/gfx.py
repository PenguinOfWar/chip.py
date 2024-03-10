import tkinter as tk
from typing import TypedDict
from tkinter import ttk
from tkinter.messagebox import showinfo
from calendar import month_name
from datetime import datetime


# set typings
class ScreenSize(TypedDict):
    width: int
    height: int


class CenterPos(TypedDict):
    x: int
    y: int


class Gfx(object):

    def __init__(self):
        # chip-8 has a screen resolution of 64x32
        # we will use a configurable scale defaulting to 10
        self.width = 64
        self.height = 32
        self.scale = 10
        self.tk = tk.Tk()
        self.spacing = 20

    def boot(self):
        # get screen dimensions
        screen = self.get_screen_size()
        center = self.get_screen_center(screen)

        # set tkinter screen size
        self.tk.geometry(
            f'{screen["width"]+self.spacing}x{screen["height"]+self.spacing+100}+{center["x"]}+{center["y"]}'
        )

        # prevent resizing
        self.tk.resizable(False, False)

        self.tk.title("CHIP.py")

        # label
        label = ttk.Label(text="Please select a month:")
        label.pack(fill=tk.X, padx=5, pady=5)

        # create a combobox
        selected_month = tk.StringVar()
        month_cb = ttk.Combobox(self.tk, textvariable=selected_month)

        # get first 3 letters of every month name
        month_cb["values"] = [month_name[m][0:3] for m in range(1, 13)]

        # prevent typing a value
        month_cb["state"] = "readonly"

        # place the widget
        month_cb.pack(fill=tk.X, padx=5, pady=5)

        # bind the selected value changes
        def month_changed(event):
            """handle the month changed event"""
            showinfo(title="Result", message=f"You selected {selected_month.get()}!")

        month_cb.bind("<<ComboboxSelected>>", month_changed)

        # set the current month
        current_month = datetime.now().strftime("%b")
        month_cb.set(current_month)

        canvas = tk.Canvas(
            self.tk, width=screen["width"], height=screen["height"], bg="black"
        )
        canvas.pack(anchor=tk.CENTER, expand=True)

        canvas.create_rectangle((10, 10), (0, 0), fill="green", outline="green")

        self.tk.lift()
        self.tk.attributes("-topmost", True)
        self.tk.after_idle(self.tk.attributes, "-topmost", False)

        return self.tk.mainloop()

    #  returns the screen dimensions in pixels
    def get_screen_size(self) -> ScreenSize:
        return {
            "width": self.width * self.scale,
            "height": self.height * self.scale,
        }

    def get_screen_center(self, screen_size: ScreenSize) -> CenterPos:
        screen_width = self.tk.winfo_screenwidth()
        screen_height = self.tk.winfo_screenheight()

        # find the center point
        return {
            "x": int(screen_width / 2 - screen_size["width"] / 2),
            "y": int(screen_height / 2 - screen_size["height"] / 2),
        }
