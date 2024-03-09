from typing import TypedDict
import tkinter as tk


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

    def boot(self):
        # get screen dimensions
        screen = self.get_screen_size()
        center = self.get_screen_center(screen)

        # set tkinter screen size
        self.tk.geometry(
            f'{screen["width"]}x{screen["height"]}+{center["x"]}+{center["y"]}'
        )

        # prevent resizing
        self.tk.resizable(False, False)

        self.tk.title("CHIP.py")

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
