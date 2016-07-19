'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Project Name : Provisioning Application
File Name : login.py
Version : 0.1
Author : Abhay Gupta
Date : 14-09-2015
Description : This script is used for getting username and password of the user and 
authenticate it using Symportal's authentication REST API.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#!/usr/bin/python

from Tkinter import *
import requests, subprocess
import constants
#import init_provisioning


class LoginApp:
  def __init__(self, master):
    frame2 = Frame(master)
    frame2.grid()
    frame = Frame(master)
    frame.grid()

    self.message=Label(frame2, text="Please Login to proceed", fg="black", pady = 10)
    self.message.grid(columnspan=2, sticky=N)

    self.username_lbl=Label(frame, text="Username", fg="black").grid(row=0, column=0, padx = 50,pady = 25)
    self.pdw_lbl=Label(frame, text="Password", fg="black").grid(row=1, padx = 50,column=0)

    self.username = Entry(frame, width=25)
    self.username.grid(row=0, column=1)
    self.username.focus_set()
    self.password = Entry(frame, show = "*", width=25)
    self.password.grid(row=1, column=1)

    self.login_btn = Button(frame,text="Login",command=self.authenticate).grid(row=2, column=0, sticky=E, pady = 10, padx = 10)
    self.cancel_btn = Button(frame, text="Cancel", fg="red",command=frame.quit).grid(row=2, column=1, sticky=W, pady = 10, padx = 10)
    #On Pressing Enter
    root.bind("<Return>", lambda event: self.clickButton(event))

  def authenticate(self):
    username=self.username.get()
    password=self.password.get()
    self.message.configure(text="Authenticating...")
    if username != '' and password !='' and username != None and password != None:
        url = constants.URL_AUTHENTICATE
        print url
        try:
            response = requests.get(url, auth=(username, password), timeout=10, verify=False)
            if response.status_code == 200:
	            #message=init_provisioning.main(username, password)
	            message = subprocess.Popen(['python','init_provisioning.py', username, password])
	            root.quit()
            else:
                self.message.configure(text= "Authentication failed!")  
                self.message.configure(fg = 'red')
        except Exception as e:
            self.message.configure(text= "Server issue.")
            print e
            self.message.configure(fg = 'red')
    else:
        self.message.configure(text="username/password cannot be left blank.")
        self.message.configure(fg = 'red')

  def clickButton(self, event):
    try:
        widget = root.focus_get()
        if widget != root:
            widget.invoke()
    except Exception:
        #Catch exception for widgets not having invoke() method and do nothing
        pass
        #self.message.configure(text= constants.GENERAL_ERROR_MSG)          
      
root = Tk()
root.wm_title("Symstream Provisioning Application")
#For removing maximize button
root.resizable(0,0)
w = 400 # width for the Tk root
h = 200 # height for the Tk root

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
