from tkinter import *
import settings
import utils

root = Tk()

#override window settings
root.configure(bg = 'black')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')#change window size
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

#run windows
root.mainloop()