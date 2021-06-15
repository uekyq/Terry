from tkinter import *
from PIL import ImageTk, Image
root = Tk()
image1 = Image.open("dune.jpg")
def swapImg():
    print(image1.size)
    return 1
# This line resizes the image to one fourth its original size, but I think it'd be
# better to make a function that detects if the image is larger than the current window
# size and tries to resize the image by one integer factor lower until it completely fits
# within the window. Look up how to do this at work tomorrow.
def scaleImage(imageSize):
    windowDimensions = (1600,900)
    imageHeight = 800
    imageWidth = 800
    i = 1
    while(imageWidth > windowDimensions[0] and imageHeight > windowDimensions[1]):
        i = i + 0.1
        imageWidth = imageWidth / i
        imageHeight = imageHeight / i
        print(imageWidth)
        print(imageHeight)
    imageDimensions = (imageWidth, imageHeight)
    return imageDimensions
test = ImageTk.PhotoImage(image1)
label1 = Label(image=test)
label1.image = test
b = Button ( master=root, command=scaleImage(image1.size), text="ee")
label1.pack()
b.pack()
root.mainloop()