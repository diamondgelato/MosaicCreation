from tkinter import *
import tkinter as tk
from tkinter import filedialog, Text
from PIL import Image,ImageTk
import pytesseract as pt
from pytesseract import Output
import cv2
import numpy as np
import os

def choose_file():

    global filepath, img_resize
    filepath = filedialog.askopenfilename(initialdir = 'E:\\',title = 'Select an Image',filetypes = (('JPG','*.jpg'),('All files','*.*')))
    img = cv2.imread(filepath)
    img_resize = cv2.resize(img,(500,500))
    cv2.imshow('Image', img_resize)
    
    
def showtext():
    content = "Welcome To Photo-Mosaic!!!!!!!!! \nCreate custom photo mosaics with\nthe #1 Photo Mosaic App!\nThis App analyzes the colors and\nshapes of your pictures in a\nmatter of seconds to create your\npersonalized photo mosaic right\nbefore your eyes."
    textbox = tk.Frame(frame,bg = 'green')
    textbox.place(relx = 0.2,rely = 0.2,relwidth =0.6,relheight =0.6)
    text_frame = Text(textbox,bg = '#89cfef')
    text_frame.insert('2.0',content)
    text_frame.pack()


def save():
    file_save = filedialog.asksaveasfile(mode = 'w' , defaultextension = ".jpg",filetypes = (('JPG','*.jpg'),('All files','*.*')))
    img_mosaic.save(file_save)


def exit_app():
    root.quit()



root = tk.Tk()

canvas = tk.Canvas(root,height = 800,width = 800,bg = '#d71b3b') 
canvas.pack()

frame = tk.Frame(root,bg = '#e8d71e')
frame.place(relx = 0.2,rely = 0.1,relwidth =0.6,relheight =0.6)

label=tk.Label(frame,text='  PHOTO-MOSAIC',fg='#8f00ff',bg='#e8d71e',font=('Bauhaus 93',28))
label.place(relx=0.20,rely=0.1)

text_box=tk.Frame(frame,bg='#16acea')
text_box.place(relwidth=0.6,relheight=0.6,relx=0.2,rely=0.2)

openfile = tk.Button(canvas,text = 'Choose a File',fg = '#12a4d9',padx = 10,pady = 5,font=('Bauhaus 93',14), command = choose_file )
openfile.place(x = 50 , y = 640)

Mosaic_btn = tk.Button(canvas,text = '   Create Mosaic  ',fg = '#6f2da8',padx = 10,font=('Bauhaus 93',14),pady = 5)
Mosaic_btn.place(x = 320, y = 640)

Save_img_btn = tk.Button(canvas,text = 'Save Image',fg = '#0b6623',padx = 10,pady = 5,font=('Bauhaus 93',14), command = save)
Save_img_btn.place(x = 625, y = 640)

about_btn = tk.Button(canvas,text = 'Info (i)',fg = 'blue',padx = 10,pady = 5,font=('Bauhaus 93',12), command = showtext)
about_btn.place(x = 50, y = 50)

exit_btn = tk.Button(canvas,text = 'Close',fg = 'red',padx = 10,pady = 5,font=('Bauhaus 93',12), command = exit_app)
exit_btn.place(x = 700, y = 50)

root.mainloop()
