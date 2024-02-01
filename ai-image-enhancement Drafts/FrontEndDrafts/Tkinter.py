import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
import PIL
from PIL import ImageTk
from PIL import Image
from dash import html


main = Tk()
main.title("Image Enhancer")


upload = Button(main, text = "Upload Image", command=lambda:upload_file())#.grid(row=2,column=1, columnspan=4)
upload.pack(padx=1, pady= 1)
enhance = Button(main, text = "Enhance", command= lambda:enhance_file())#.grid(row=2,column=10, columnspan=4)
enhance.pack(padx=2, pady= 2)
removeImage = Button (main, text = "remove Image", command = lambda:remove_file())
removeImage.pack(padx = 1, pady= 1)

def upload_file():
    files = [('Jpg Files', '*.jpg'),('PNG Files', '*.png'), ('JPEG Files', '*.jpeg')]
    global filesName
    filesName = tk.filedialog.askopenfilename(filetypes= files)
    global img 
    img = Image.open(filesName)
    img = img.resize((500,500))
    img = ImageTk.PhotoImage(img)
    global e1
    e1 = tk.Label(main)
    e1.pack(side = LEFT)
    e1.image = img
    e1['image'] = img

def enhance_file():
    global e2
    e2 = tk.Label(main)
    e2.pack(side = RIGHT)
    e2.image = img
    e2['image'] = img
    
#this section will be connected to the ehnanced model I will be making


def remove_file():
    img.close()
    

main.geometry("10000x1000")
main.mainloop()