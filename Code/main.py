import cv2
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
from PIL import ImageTk, Image
import joblib
import sklearn

def LoadImg():
    tkinter.messagebox.showwarning("Warning", "Image must be an 28x28")
    filename = filedialog.askopenfilename(initialdir="/",title="Select a File",filetypes=(("imgaes","*.jpg*"),("all files","*.*")))
    global img
    img = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
    im = Image.fromarray(img)
    img = img.reshape(1, -1)
    img = cv2.bitwise_not(img)
    imgtk = ImageTk.PhotoImage(image=im)
    imageLabel.configure(image=imgtk)
    imageLabel.image = imgtk
def recognize():

    model = joblib.load('DigitRecognision')
    result = model.predict(img)
    ResultText = "Predicted digit: "+result
    tkinter.messagebox.showinfo("Result",ResultText)

bgwindow = "#8C8C8C"
bgbutton = "#C8C8C8"

window = Tk()
window.title("Recognize digit")
window.geometry("300x200")
window.configure(bg=bgwindow)
frame = Frame(window, bg = bgwindow)
frame.pack()

load = Button(frame, text = "Load image", command=LoadImg,borderwidth = 4 ,bg = bgbutton)
load.pack(side = "top", fill="x")
recognize = Button(frame, text = "Recognize using AI", command=recognize,borderwidth = 4,bg = bgbutton )
recognize.pack(side = "top", fill="x")
capt = Label(frame,text = "Preview image",font = ("Arial",10), bg = bgwindow)
capt.pack()
imageLabel = Label(frame, bg = bgwindow)
imageLabel.pack()


window.mainloop()
