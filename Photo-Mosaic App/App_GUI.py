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
    cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
    cv2.imshow('frame', img)
     

def create_mosaic():
    
    def manual_click():
        top_new = Toplevel()
        entry = Entry(top_new, width = 40, borderwidth = 7)
        entry.pack()
        entry.insert(1,"Enter Number Of Pieces")

        def enter():
            print(entry.get())
            top_new.destroy()
            
        enter_btn = tk.Button(top_new,text = 'Enter',fg = 'purple',padx = 10,pady = 5,font=('Bauhaus 93',10),command = enter)
        enter_btn.pack()

    top = Toplevel()

    canvas_new = tk.Canvas(top,height = 600,width = 600,bg = '#d71b3b') 
    canvas_new.pack()

    label_new1=tk.Label(canvas_new,text='Photo-Mosaic!!!!',fg='#16acea',bg='#e8d71e',font=('Bauhaus 93',48))
    label_new1.place(relx = 0.08 ,rely = 0.8)

    frame_new = tk.Frame(top,bg = '#e8d71e')
    frame_new.place(relx = 0.2,rely = 0.1,relwidth =0.6,relheight =0.6)


    Mosaic_btn_manual = tk.Button(frame_new,text = 'Create The Mosaic Manually?',fg = 'navy',padx = 10,font=('Bauhaus 93',14),pady = 5, command = manual_click)
    Mosaic_btn_manual.place(relx = 0.12, rely = 0.25)

    Mosaic_btn_auto = tk.Button(frame_new,text = 'Create The Mosaic Automatically?',fg = 'navy',padx = 10,font=('Bauhaus 93',14),pady = 5)
    Mosaic_btn_auto.place(relx = 0.05, rely = 0.55)

    label_new=tk.Label(frame_new,text = '--OR--',fg='#a9a9a9',bg='#e8d71e',font=('Bauhaus 93',22))
    label_new.place(relx = 0.42 ,rely = 0.42)

    exit_btn_new = tk.Button(canvas_new,text = 'Back<<<',fg = 'red',padx = 10,pady = 5,font=('Bauhaus 93',12), command = top.destroy)
    exit_btn_new.place(relx = 0.83, rely = 0.063)


def black_white():
    global im_color2
    im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    im_color2 = cv2.applyColorMap(im_gray,cv2.COLORMAP_BONE)
    cv2.namedWindow('Vintage',cv2.WINDOW_NORMAL)
    cv2.imshow('Vintage',im_color2)
    

def filter_hsv():
    global im_color
    im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    im_color = cv2.applyColorMap(im_gray,cv2.COLORMAP_HSV)
    cv2.namedWindow('Negative',cv2.WINDOW_NORMAL)
    cv2.imshow('Negative',im_color)
    

def filter_plasma():
    global im_color3
    im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    im_color3 = cv2.applyColorMap(im_gray,cv2.COLORMAP_CIVIDIS)
    cv2.namedWindow('Dim',cv2.WINDOW_NORMAL)
    cv2.imshow('Dim',im_color3)
    

def filter_ocean():
    global im_color1
    im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    im_color1 = cv2.applyColorMap(im_gray,cv2.COLORMAP_OCEAN)
    cv2.namedWindow('Ocean',cv2.WINDOW_NORMAL)
    cv2.imshow('Ocean',im_color1)
 
   
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
label.place(relx = 0.24 ,rely = 0.8)

text_box=tk.Frame(frame,bg='#16acea')
text_box.place(relwidth=0.6,relheight=0.6,relx=0.2,rely=0.2)

openfile = tk.Button(canvas,text = 'Choose a File',fg = '#12a4d9',padx = 10,pady = 5,font=('Bauhaus 93',14), command = choose_file )
openfile.place(relx = 0.06 , rely = 0.8)

Mosaic_btn = tk.Button(canvas,text = '   Create Mosaic  ',fg = '#6f2da8',padx = 10,font=('Bauhaus 93',14),pady = 5, command = create_mosaic)
Mosaic_btn.place(relx = 0.39, rely = 0.8)


TakePhoto_btn = tk.Button(canvas,text = 'Take A Photo',fg = '#0b6623',padx = 10,pady = 5,font=('Bauhaus 93',14))
TakePhoto_btn.place(relx = 0.76, rely = 0.8)

Save_img_btn = tk.Button(canvas,text = 'Save Image',fg = 'brown',padx = 10,pady = 5,font=('Bauhaus 93',10), command = save)
Save_img_btn.place(relx = 0.83, rely = 0.9)

about_btn = tk.Button(canvas,text = 'Info (i)',fg = 'blue',padx = 10,pady = 5,font=('Bauhaus 93',12), command = showtext)
about_btn.place(relx = 0.063, rely = 0.063)

filter_bw = tk.Button(frame,text = 'Vintage',fg = 'black',padx = 10,pady = 5,font=('Bauhaus 93',10), command = black_white)
filter_bw.place(relx =0.05 , rely =0.9)

filter_plasma = tk.Button(frame,text = '   Dim   ',fg = 'orange',padx = 10,pady = 5,font=('Bauhaus 93',10), command = filter_plasma)
filter_plasma.place(relx = 0.3, rely = 0.9)

filter_ocean = tk.Button(frame,text = 'Ocean',fg = 'navy',padx = 10,pady = 5,font=('Bauhaus 93',10), command = filter_ocean)
filter_ocean.place(relx = 0.56, rely = 0.9)

filter_negative = tk.Button(frame,text = 'Negative',fg = 'lime',padx = 10,pady = 5,font=('Bauhaus 93',10), command = filter_hsv)
filter_negative.place(relx = 0.79, rely = 0.9)


exit_btn = tk.Button(canvas,text = 'Close (X)',fg = 'red',padx = 10,pady = 5,font=('Bauhaus 93',12), command = exit_app)
exit_btn.place(relx = 0.83,rely = 0.063)

root.mainloop()
