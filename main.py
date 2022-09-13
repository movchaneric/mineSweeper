from tkinter import *
from cell import Cell
import settings
import utils

root = Tk()

#override window settings
root.configure(bg = 'black')
#change window size
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Minesweeper Game')
root.resizable(width=False, height=False)

#frames configure
top_frame = Frame(root,
                  bg = "black",
                  width = settings.WIDTH,
                  height = utils.height_percentage(25))
top_frame.place(x = 0, y = 0)

left_frame = Frame(root,
                   bg = "black",
                   width = utils.width_percentage(25),
                   height = utils.height_percentage(75))
left_frame.place(x = 0, y = utils.height_percentage(25))

center_frame = Frame(root,
                     bg = "black",
                     width = utils.width_percentage(75),
                     height = utils.height_percentage(75))
center_frame.place(x = utils.width_percentage(25), y = utils.height_percentage(25))

#create 25 buttons
for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn(center_frame)
        c.cell_button_object.grid(column = x, row = y)

#call the label from the Cell class and position it on the left side
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x = 0, y = 0)

Cell.randomize_mines()

#run windows
root.mainloop()