from tkinter import *
from PIL import ImageTk, Image

root = Tk()

# ee
# Creating a Label Widget
myLabel = Label(root, text="Hello, World!")
myLabel.pack()
canvas = Canvas(root, width = 300, height = 300)
canvas.pack()
img = ImageTk.PhotoImage(file="C:/Users/Uekyq/Documents/Scripts/Python/tkinter/unicorn.jpg")
img2 = ImageTk.PhotoImage(file="C:/Users/Uekyq/Documents/Scripts/Python/tkinter/unicorn2.jpg")
canvas.create_image(20,20, anchor=NW, image=img)
def swapImg():
    canvas.create_image(20,20, anchor=NW, image=img2)
    return 1
b = Button ( master=root, command=swapImg, text="ee")
b.pack()

root.mainloop()
