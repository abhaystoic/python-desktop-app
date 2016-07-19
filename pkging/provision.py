'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
File Name : login.py
Version : 0.1
Author : Abhay Gupta
Date : 14-09-2015
Description : This script is used for getting username and password of the user and 
authenticate it using Symportal's authentication REST API.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#!/usr/bin/python

from Tkinter import *
import requests
import init_provisioning

class LoginApp:
  def __init__(self, master):
    frame = Frame(master)
    frame.grid()

    self.username_lbl=Label(frame, text="Enter username", fg="black").grid(row=0, column=0, padx = 30, pady = 15)
    self.pdw_lbl=Label(frame, text="Enter password", fg="black").grid(row=1, column=0, padx = 30)

    self.username = Entry(frame, width=25)
    self.username.grid(row=0, column=1)
    self.password = Entry(frame, show = "*", width=25)
    self.password.grid(row=1, column=1)

    self.login_btn = Button(frame,text="Login",command=self.authenticate).grid(row=2, column=0, sticky=E, pady = 10)
    self.cancel_btn = Button(frame, text="Cancel", fg="red",command=frame.quit).grid(row=2, column=1, sticky=W, pady = 10)

    self.message=Label(frame, text="Please Login to proceed", fg="black", pady = 2)
    self.message.grid(columnspan=2, sticky=N+S+E+W)
  def authenticate(self):
    username=self.username.get()
    password=self.password.get()
    self.message.configure(text="Authenticating...")
    if username != '' and password !='' and username != None and password != None:
        url="http://localhost:8000/symportal/authenticate"
        response=requests.get(url, auth=(username, password), timeout=30)
        if response.status_code == 200:
            message=init_provisioning.main(username, password)
            root.quit()
        else:
            self.message.configure(text= "Authentication failed!")  
    else:
        self.message.configure(text="username/password cannot be left blank.")


root = Tk()
root.wm_title("Authenticate Yourself")
#For removing maximize button
root.resizable(0,0)
w = 400 # width for the Tk root
h = 150 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
app = LoginApp(root)
root.mainloop()