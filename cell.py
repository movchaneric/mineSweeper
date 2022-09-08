from tkinter import Button
import settings
import random

import settings


class Cell:
    all = []
    #constructor
    def __init__(self, x, y , is_mine = False):
        self.is_mine = is_mine
        self.cell_button = None
        self.x = x
        self.y = y

        #append object to Cell.all list
        Cell.all.append(self)

    def create_btn(self, btn_location):
        btn = Button(
            btn_location,
            width = 12,
            height = 4,
            text = f"{self.x}, {self.y}"
        )
        btn.bind('<Button-1>', self.left_click_action) #left click
        btn.bind('<Button-2>', self.right_click_action) #right click #problem => doesnt right click
        self.cell_button = btn

    def left_click_action(self, event):
        print(event)
        print("left button clicked")


    def right_click_action(self, event):
        print(event)
        print("right button clicked")

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, settings.MINES_COUNT)

        for picked_cell in picked_cells:
            picked_cell.is_mine = True


    def __repr__(self):
        return f"Cell({self.x}, {self.y})"