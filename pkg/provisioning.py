from Tkinter import *
import subprocess, test
class App:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()

    self.message=Label(root, text="Welcome to Modem Provisioing App", fg="black")
    self.message.pack(side=TOP,fill=X)

    self.slogan = Button(frame,
                         text="Update",
                         command=self.call_script)
    self.slogan.pack(side=LEFT)

    self.button = Button(frame, 
                         text="QUIT", fg="red",
                         command=frame.quit)
    self.button.pack(side=LEFT)

  def call_script(self):
    message=test.test()
    self.message['text'] = message

root = Tk()
root.wm_title("Modem Provisioing APP")
w = 700 # width for the Tk root
h = 350 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
app = App(root)
root.mainloop()