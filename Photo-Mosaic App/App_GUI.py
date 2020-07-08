from tkinter import *
import tkinter as tk
from tkinter import filedialog, Text
from PIL import Image,ImageTk
import cv2
import numpy as np



    
def choose_file():

    global filepath, img
    filepath = filedialog.askopenfilename(initialdir = 'E:\\',title = 'Select an Image',filetypes = (('JPG','*.jpg'),('All files','*.*')))
    img = cv2.imread(filepath)
    cv2.namedWindow('frame',cv2.WINDOW_GUI_NORMAL)
    cv2.imshow('frame', img)
    cv2.waitKey(0) 


def black_white():
    global im_color2
    im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    im_color2 = cv2.applyColorMap(im_gray,cv2.COLORMAP_BONE)
    cv2.namedWindow('image2',cv2.WINDOW_NORMAL)
    cv2.imshow('image2',im_color2)
    cv2.waitKey(0)

def filter_hsv():
    global im_color
    im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    im_color = cv2.applyColorMap(im_gray,cv2.COLORMAP_HSV)
    cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    cv2.imshow('image',im_color)
    cv2.waitKey(0)

def filter_plasma():
    global im_color3
    im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    im_color3 = cv2.applyColorMap(im_gray,cv2.COLORMAP_CIVIDIS)
    cv2.namedWindow('image3',cv2.WINDOW_NORMAL)
    cv2.imshow('image3',im_color3)
    cv2.waitKey(0)

def filter_ocean():
    global im_color1
    im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    im_color1 = cv2.applyColorMap(im_gray,cv2.COLORMAP_OCEAN)
    cv2.namedWindow('image1',cv2.WINDOW_NORMAL)
    cv2.imshow('image1',im_color1)
    cv2.waitKey(0)  

  
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

label=tk.Label(frame,text='~~~~FILTERS~~~~',fg='#a9a9a9',bg='#e8d71e',font=('Bauhaus 93',22))
label.place(x = 110 ,y = 390)

text_box=tk.Frame(frame,bg='#16acea')
text_box.place(relwidth=0.6,relheight=0.6,relx=0.2,rely=0.2)

openfile = tk.Button(canvas,text = 'Choose a File',fg = '#12a4d9',padx = 10,pady = 5,font=('Bauhaus 93',14), command = choose_file )
openfile.place(x = 50 , y = 640)

Mosaic_btn = tk.Button(canvas,text = '   Create Mosaic  ',fg = '#6f2da8',padx = 10,font=('Bauhaus 93',14),pady = 5)
Mosaic_btn.place(x = 320, y = 640)

TakePhoto_btn = tk.Button(canvas,text = 'Take A Photo',fg = '#0b6623',padx = 10,pady = 5,font=('Bauhaus 93',14))
TakePhoto_btn.place(x = 625, y = 640)

Save_img_btn = tk.Button(canvas,text = 'Save Image',fg = 'brown',padx = 10,pady = 5,font=('Bauhaus 93',10), command = save)
Save_img_btn.place(x = 680, y = 730)

about_btn = tk.Button(canvas,text = 'Info (i)',fg = 'blue',padx = 10,pady = 5,font=('Bauhaus 93',12), command = showtext)
about_btn.place(x = 50, y = 50)

filter_bw = tk.Button(frame,text = 'Vintage',fg = 'black',padx = 10,pady = 5,font=('Bauhaus 93',10), command = black_white)
filter_bw.place(x =25 , y =445)

filter_plasma = tk.Button(frame,text = '   Dim   ',fg = 'orange',padx = 10,pady = 5,font=('Bauhaus 93',10), command = filter_plasma)
filter_plasma.place(x = 155, y = 445)

filter_ocean = tk.Button(frame,text = 'Ocean',fg = 'navy',padx = 10,pady = 5,font=('Bauhaus 93',10), command = filter_ocean)
filter_ocean.place(x = 275, y = 445)

filter_negative = tk.Button(frame,text = 'Negative',fg = 'lime',padx = 10,pady = 5,font=('Bauhaus 93',10), command = filter_hsv)
filter_negative.place(x = 380, y = 445)

exit_btn = tk.Button(canvas,text = 'Close',fg = 'red',padx = 10,pady = 5,font=('Bauhaus 93',12), command = exit_app)
exit_btn.place(x = 700, y = 50)

root.mainloop()
