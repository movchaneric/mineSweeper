import tkinter.messagebox

from tkmacosx import Button
from tkinter import Label
import random
import settings
import ctypes


class Cell:
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None
    #constructor
    def __init__(self, x, y , is_mine = False):
        self.is_mine = is_mine
        self.cell_button_object = None
        self.is_opened = False
        self.is_mine_candidate = False
        self.x = x
        self.y = y

        #append object to Cell.all list
        Cell.all.append(self)

    def create_btn(self, btn_location):
        btn = Button(
            btn_location,
            width = 120,
            height = 80
        )
        btn.bind('<Button-2>', self.right_click_action) #right mouse click
        btn.bind('<Button-1>', self.left_click_action) #left mouse click

        self.cell_button_object = btn

    @staticmethod
    def create_cell_count_label(location):
        label = Label(
            location,
            text = f"Cells Left: {Cell.cell_count}",
            font = ("Ariel",35),
            bg = "black",
            fg = "white"
        )
        Cell.cell_count_label_object = label


    # button click actions:
    def left_click_action(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            #len = 0 means no mined cell => open all surrounded cells
            if (self.surrounded_cell_length == 0):
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()

    def right_click_action(self, event):
        if not self.is_mine_candidate:
            self.cell_button_object.configure(bg = "orange")
            self.is_mine_candidate = True
        else:
            if (self.is_mine_candidate):
                self.cell_button_object.configure(
                    bg = 'SystemButtonFace'
                )
                self.is_mine_candidate = False


    def get_cell_by_cord(self, x, y):
        # Return cell based on the values x and y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    def show_mine(self):
        #logic to interapt the game and display messege that player lost
        tkinter.messagebox.showerror(title = "Game over",message= "You have lost the game")
        self.cell_button_object.configure(bg= 'red')


    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_cord(self.x - 1, self.y - 1),
            self.get_cell_by_cord(self.x - 1, self.y),
            self.get_cell_by_cord(self.x - 1, self.y + 1),
            self.get_cell_by_cord(self.x, self.y - 1),
            self.get_cell_by_cord(self.x + 1, self.y - 1),
            self.get_cell_by_cord(self.x + 1, self.y),
            self.get_cell_by_cord(self.x + 1, self.y + 1),
            self.get_cell_by_cord(self.x, self.y + 1),
        ]
        # eliminate None from showing inside the list
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cell_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1;
        return counter

    # game logic
    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_button_object.configure(text = str(self.surrounded_cell_length))
            # Replace the text of the cell count label with the newer count
            if(Cell.cell_count_label_object):
                Cell.cell_count_label_object.configure(
                    text = f"Cells Left: {Cell.cell_count}"
                )
        self.is_opened = True

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, settings.MINES_COUNT)

        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"