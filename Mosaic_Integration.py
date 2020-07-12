from tkinter import *
import tkinter as tk
from tkinter import filedialog, Text
from tkinter import simpledialog
from PIL import Image,ImageTk
import cv2
import numpy as np
import random as rd
import sys
sys.path.append('MosaicPieces')
import ControlPieces as CT
#used to save image
my_image=np.zeros((),np.uint8)

# used to browse a file from the folder
def choose_file():

    global filepath, pic,my_image
    filepath = filedialog.askopenfilename(initialdir = 'E:\\',title = 'Select an Image',filetypes = (('JPG','*.jpg'),('All files','*.*')))
    pic = cv2.imread(filepath)
    my_image=pic.copy()
    cv2.namedWindow('original',cv2.WINDOW_NORMAL)
    cv2.imshow('original', pic)


def webcam():
    global shot ,my_image,pic
    cap=cv2.VideoCapture(0)
    while True:
        ret,shot=cap.read() 
        cv2.imshow("frame",shot)
        count=0
        k=cv2.waitKey(1)
        if  k==ord(" ")  : #space bar to get a screenshot
            pic=shot.copy()
            cv2.imshow("frame",shot)
            break
      
        
    cap.release()
   

def create_mosaic():
    # manually make mosaic after giving an input of pieces.
    def manual():
        global pieces ,my_image
        pieces=simpledialog.askinteger("Input Pieces", "Enter the no. of Pieces")
        print(pieces)
        mosaicPiece = CT.getMosaic (pic, pieces)
        img_gray=cv2.cvtColor(mosaicPiece,cv2.COLOR_BGR2GRAY)
        ret,thresh=cv2.threshold(img_gray,1,255,cv2.THRESH_BINARY)
        contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
        for contour in contours:
            approx=cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour,True),True)
            cv2.drawContours(mosaicPiece,[approx],0,(0,255,0),5)
            area=cv2.contourArea(contour)
        
            if(area>100):
                M=cv2.moments(contour)
                cx=int(M["m10"] / M["m00"])
                cy=int(M["m01"] / M["m00"])
                print(mosaicPiece[cy][cx])
                b=int(mosaicPiece[cy][cx][0])
                g=int(mosaicPiece[cy][cx][1])
                r=int(mosaicPiece[cy][cx][2])
                print(b)
                print(g)
                print(r)
                cv2.fillPoly(mosaicPiece,pts=[contour],color=(b,g,r))
        my_image=mosaicPiece.copy()        
        cv2.namedWindow('original', cv2.WINDOW_NORMAL)        
        cv2.imshow ('original', mosaicPiece)
        
    # Automatically create traingular Mosaic for selected image.
    def triangular_mosaic():
        global my_image
        img_gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
        ret, global_thresh = cv2.threshold(img_gray, 1, 255, cv2.THRESH_BINARY)
        width = global_thresh.shape[1]
        height = global_thresh.shape[0]
        rect = (0, 0, width, height)
        subdiv = cv2.Subdiv2D(rect)

        # points on the inside

        # selects 100 random points on the image
        for i in range(0, 100):
            randx = rd.randint(0, width)

            randy = rd.randint(0, height)
            subdiv.insert((randx, randy))

        # edge points

        # selects 10 random points on each side
        for i in range(0, 10):
            subdiv.insert((0, rd.randint(0, height)))
            subdiv.insert((rd.randint(0, width), 0))
            subdiv.insert((width-1, rd.randint(0, height)))
            subdiv.insert((rd.randint(0, width), height-1))

        # corners

        subdiv.insert((0, 0))
        subdiv.insert((0, height-1))
        subdiv.insert((width-1, 0))
        subdiv.insert((width-1, height-1))

        triangleList = subdiv.getTriangleList()

        for t in triangleList:
            pt1 = (t[0], t[1])
            pt2 = (t[2], t[3])
            pt3 = (t[4], t[5])

            # draws the triangles

            cv2.line(global_thresh, pt1, pt2, (0, 0, 0), 5)
            cv2.line(global_thresh, pt2, pt3, (0, 0, 0), 5)
            cv2.line(global_thresh, pt1, pt3, (0, 0, 0), 5)

        contours, hierarchy = cv2.findContours(global_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        for contour in contours:
           
            approx=cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour,True),True)
            cv2.drawContours(pic,[approx],0,(0,0,0),2)
            x = approx.ravel()[0]
            y = approx.ravel()[1]
          
            area=cv2.contourArea(contour)
            if(area>100):
                M=cv2.moments(contour)
                cx=int(M["m10"] / M["m00"])
                cy=int(M["m01"] / M["m00"])
                
                print(pic[cy][cx])
                b=int(pic[cy][cx][0])
                g=int(pic[cy][cx][1])
                r=int(pic[cy][cx][2])
                print(b)
                print(g)
                print(r)
                cv2.fillPoly(pic,pts=[contour],color=(b,g,r))
        my_image=pic.copy()        
        cv2.namedWindow('original', cv2.WINDOW_NORMAL)
        cv2.imshow('original', pic)
        
        
    top = Toplevel()
    canvas_new = tk.Canvas(top,height = 600,width = 600,bg = '#d71b3b') 
    canvas_new.pack()

    label_new1=tk.Label(canvas_new,text='Photo-Mosaic!!!!',fg='#16acea',bg='#e8d71e',font=('Bauhaus 93',48))
    label_new1.place(relx = 0.08 ,rely = 0.8)

    frame_new = tk.Frame(top,bg = '#e8d71e')
    frame_new.place(relx = 0.2,rely = 0.1,relwidth =0.6,relheight =0.6)

    Mosaic_btn_manual = tk.Button(frame_new,text = 'Create The Mosaic Manually?',fg = 'navy',padx = 10,font=('Bauhaus 93',14),pady = 5, command = manual)
    Mosaic_btn_manual.place(relx = 0.12, rely = 0.25)

    Mosaic_btn_auto = tk.Button(frame_new,text = 'Create Triangular Mosaic Automatically?',fg = 'navy',padx = 10,font=('Bauhaus 93',14),pady = 5,command=triangular_mosaic)
    Mosaic_btn_auto.place(relx = 0.05, rely = 0.55)

    label_new=tk.Label(frame_new,text = '--OR--',fg='#a9a9a9',bg='#e8d71e',font=('Bauhaus 93',22))
    label_new.place(relx = 0.42 ,rely = 0.42)

    exit_btn_new = tk.Button(canvas_new,text = 'Back<<<',fg = 'red',padx = 10,pady = 5,font=('Bauhaus 93',12), command = top.destroy)
    exit_btn_new.place(relx = 0.83, rely = 0.063)
# adding filters to the image

def filters_list():   
    def black_white():
        global im_color2 ,my_image
        im_gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
        im_color2 = cv2.applyColorMap(im_gray,cv2.COLORMAP_BONE)
        my_image=im_color2.copy()
        cv2.namedWindow('original',cv2.WINDOW_NORMAL)
        cv2.imshow('original',im_color2)


    def filter_hsv():
        global im_color ,my_image
        im_gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
        im_color = cv2.applyColorMap(im_gray,cv2.COLORMAP_HSV)
        my_image=im_color.copy()
        cv2.namedWindow('original',cv2.WINDOW_NORMAL)
        cv2.imshow('original',im_color)
        

    def filter_plasma():
        global im_color3 ,my_image
        im_gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
        im_color3 = cv2.applyColorMap(im_gray,cv2.COLORMAP_CIVIDIS)
        my_image=im_color3.copy()
        cv2.namedWindow('original',cv2.WINDOW_NORMAL)
        cv2.imshow('original',im_color3)
        

    def filter_ocean():
        global im_color1 ,my_image
        im_gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
        im_color1 = cv2.applyColorMap(im_gray,cv2.COLORMAP_OCEAN)
        my_image=im_color1.copy()
        cv2.namedWindow('original',cv2.WINDOW_NORMAL)
        cv2.imshow('original',im_color1)
        
    top_hash = Toplevel()  

    canvas_hash = tk.Canvas(top_hash,height = 500, width = 500,bg = '#d71b3b') 
    canvas_hash.pack()

    label_hash1=tk.Label(canvas_hash,text='Filters',fg='#16acea',bg='#e8d71e',font=('Bauhaus 93',38))
    label_hash1.place(relx = 0.385 ,rely = 0.8)

    frame_hash = tk.Frame(top_hash,bg = '#EFF294')
    frame_hash.place(relx = 0.2,rely = 0.1,relwidth =0.6,relheight =0.6) 

    filter_bw = tk.Button(frame_hash,text = 'Vintage',fg = 'black',padx = 54,pady = 5,font=('Bauhaus 93',14), command = black_white)
    filter_bw.place(relx =0.21 , rely =0.1)

    filter_plasma = tk.Button(frame_hash,text = 'Dim',fg = 'blue',padx = 69,pady = 5,font=('Bauhaus 93',14), command = filter_plasma)
    filter_plasma.place(relx = 0.21, rely = 0.33)

    filter_ocean = tk.Button(frame_hash,text = 'Ocean',fg = 'navy',padx = 58,pady = 5,font=('Bauhaus 93',14), command = filter_ocean)
    filter_ocean.place(relx = 0.21, rely = 0.536)

    filter_negative = tk.Button(frame_hash,text = 'Negative',fg = 'green',padx =50,pady = 5,font=('Bauhaus 93',14), command = filter_hsv)
    filter_negative.place(relx = 0.21, rely = 0.76)

    exit_btn_hash = tk.Button(canvas_hash,text = 'Back<<<',fg = 'red',padx = 10,pady = 5,font=('Bauhaus 93',10), command = top_hash.destroy)
    exit_btn_hash.place(relx = 0.81, rely = 0.063)

def showtext():
    content = "Welcome To Photo-Mosaic!! \nMosaic Photo Effects is an easy to use and powerful app to create amazing mosaic pictures.\nTransform any of your pictures into Mosaic photo and create amazing mosaic photo collage using Mosaic Photo Effects.\nMosaic Photo Effects, convert your photos into an Art. You can now make a Mosaic Photo just in some few steps. \nThis Mosaic Making app makes high quality mosaic photo collages."
    textbox = tk.Frame(frame,bg = 'green')
    textbox.place(relx = 0.2,rely = 0.2,relwidth =0.6,relheight =0.6)
    text_frame = Text(textbox,bg = '#89cfef')
    text_frame.insert('2.0',content)
    text_frame.pack()
count=0
def save():
    name=simpledialog.askstring("Save As", "please enter the name of the file")
    cv2.imwrite(str(name)+'.jpg',my_image)


def original():
    cv2.imshow("Orignal Image",pic)   
#delete all the windows

def exit_app():
    root.quit()

root = tk.Tk()
root.title("Photo Mosaic App")
  
canvas = tk.Canvas(root,height = 800,width = 800,bg = '#d71b3b') 
canvas.pack()

frame = tk.Frame(root,bg = '#EFF294')
frame.place(relx = 0.2,rely = 0.2,relwidth =0.6,relheight =0.6)

label=tk.Label(frame,text='Mosaic Photo Maker',fg='black',bg='#EFF294',font=('Bauhaus 93',24))
label.place(relx=0.2,rely=0.1)

label=tk.Label(frame,text='---------Filters---------',fg='black',bg='#EFF294',font=('Georgia',20))
label.place(relx = 0.24 ,rely = 0.8)

text_box=tk.Frame(frame,bg='#16acea')
text_box.place(relwidth=0.6,relheight=0.6,relx=0.2,rely=0.2)

openfile = tk.Button(canvas,text = 'Browse',fg = '#12a4d9',padx = 10,pady = 5,font=('Bauhaus 93',14), command = choose_file )
openfile.place(relx = 0.045, rely = 0.4)

camera_bw = tk.Button(canvas,text = 'Webcam',fg = 'black',padx = 50,pady = 5,font=('Bauhaus 93',14), command = webcam)
camera_bw.place(relx = 0.7, rely = 0.85)


about_btn = tk.Button(canvas,text = 'Info (i)',fg = 'blue',padx = 10,pady = 5,font=('Bauhaus 93',14), command = showtext)
about_btn.place(relx = 0.045, rely = 0.1)

filter_bw = tk.Button(frame,text = 'Filters',fg = 'black',bg="#F6D8E2",padx = 50,pady = 5,font=('Bauhaus 93',14), command = filters_list)
filter_bw.place(relx =0.325 , rely =0.875)
 
mosaic_btw = tk.Button(canvas,text = 'Create Mosaic',fg = 'black',padx = 50,pady = 5,font=('Bauhaus 93',14), command = create_mosaic)
mosaic_btw.place(relx =0.35 , rely =0.85) 

original_btn = tk.Button(canvas,text = 'Original',fg = 'black',padx =50,pady = 5,font=('Bauhaus 93',14), command = original)
original_btn.place(relx = 0.045, rely = 0.85)


Save_img_btn = tk.Button(canvas,text = 'Save',fg = '#104e8b',padx = 10,pady = 5,font=('Bauhaus 93',14), command = save)
Save_img_btn.place(relx = 0.85, rely = 0.4)

exit_btn = tk.Button(canvas,text = 'Close (X)',fg = 'red',padx = 10,pady = 5,font=('Bauhaus 93',14), command = exit_app)
exit_btn.place(relx = 0.8,rely = 0.1)


root.mainloop()
