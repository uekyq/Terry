from tkinter import *
from PIL import ImageTk, Image

root = Tk()

image1 = Image.open("dune.jpg")
def swapImg():
    print(image1.size)
    return 1
# This line resizes the image to one fourth its original size, but I think it'd be better to make a functio that detects if the image is larger than the current window size and tries to resize the image by one integer factor lower until it completely fits within the window. Look up how to do this at work tomorrow.
image1 = image1.resize((int(image1.size[0] / 4),int(image1.size[1] / 4)),Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)

label1 = Label(image=test)
label1.image = test

myLabel = Label(root, text="Hello, World!")
b = Button ( master=root, command=swapImg, text="ee")
myLabel.pack()
b.pack()
label1.pack()

root.mainloop()
