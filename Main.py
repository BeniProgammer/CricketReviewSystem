#importing all the modules
import tkinter  #tkinter is for The GUI
import cv2      #cv2 is to play the video and converting the images
import PIL.Image, PIL.ImageTk #showing the images
from functools import partial #to give arguments to a funtion
import threading
import imutils
import time #time function for waiting

stream = cv2.VideoCapture("clip1.mp4")

#speed of the video function
def play(speed):
    print(f"Speed is {speed}")
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1+speed)
    grabbed, frame = stream.read()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    canvas.image = frame
    canvas.create_text(190,32, fill="light green", font="Times 34 bold", text="Decision Pending:")


#decision Pending screen function
def pending(decision):
    #converting the image in to RBG with module cv2
    imagephoto = cv2.cvtColor(cv2.imread("decisionpending.png"), cv2.COLOR_BGR2RGB)
    imagephoto = imutils.resize(imagephoto, width=SET_WIDTH, height=SET_HEIGHT)
    imagephoto = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(imagephoto))
    canvas.create_image(0,0, image=imagephoto, anchor=tkinter.NW)
    canvas.image = imagephoto
    
    #wait for 2 seconds
    time.sleep(2)

    if decision == "Out":
        decisionimg = "Out.png"
        #if decision is out then show the out image

    else:
        decisionimg = "notout.png"
        #else show the not out image

    #converting the out or not out image into RGB with cv2 module
    imagephoto = cv2.cvtColor(cv2.imread(decisionimg), cv2.COLOR_BGR2RGB)
    imagephoto = imutils.resize(imagephoto, width=SET_WIDTH, height=SET_HEIGHT)
    imagephoto = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(imagephoto))
    canvas.create_image(0,0, image=imagephoto, anchor=tkinter.NW)
    canvas.image = imagephoto


#funtion for declaring the player out   
def out():
    thread = threading.Thread(target=pending, args=('Out',))
    thread.daemon = 1
    thread.start()
    print('Player is out')

#funtion for declaring the player not out  
def NotOut():
        thread = threading.Thread(target=pending, args=('Not Out',))
        thread.daemon = 9
        thread.start()
        print("Player is Not out")

#width and height of the screen 
SET_WIDTH = 1280
SET_HEIGHT = 720

#starting screen
window = tkinter.Tk()
window.title('Third Umpire Decision review System')
cv_img = cv2.cvtColor(cv2.imread("welcome.png"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, ancho=tkinter.NW, image=photo)
canvas.pack()

#controls
btn = tkinter.Button(window, text= "< Previous Frame >", width=50, command=partial(play,-2))
btn.pack()
btn2 = tkinter.Button(window, text= "< Next Frame >", width=50, command=partial(play,2))
btn2.pack()
btn3 = tkinter.Button(window, text= "< Declare out >", width=50, command=out)
btn3.pack()
btn4 = tkinter.Button(window, text= "< Declare not out >", width=50, command=NotOut)
btn4.pack()

#main loop
window.mainloop()