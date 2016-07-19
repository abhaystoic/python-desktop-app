'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
File Name : init_provisioning.py
Version : 0.1
Author : Abhay Gupta
Date : 14-09-2015
Description : This script is called after the user is successfully logged in. It is used for 
calling prov.py script, validating the data received and calling Symportal's REST API for 
updating certificate in the database.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#!/usr/bin/python

from Tkinter import *
import fetch, time, requests, sys
import constants

class App:
  def __init__(self, root, username, password):
    frame = Frame(root)
    frame.pack()

    self.message2=Label(root, text="", fg="blue", pady = 10)
    self.message2.pack(side=TOP,fill=X)

    self.message3=Label(root, text="", fg="blue", pady = 10)
    self.message3.pack(side=TOP,fill=X)
    self.slogan = Button(frame,
                         text="Update",
                         command= lambda: self.call_script(root, username, password))
    self.slogan.pack(side=LEFT, pady = 35,  padx = 10)
    self.slogan.focus_set()
    self.button = Button(frame, 
                         text="QUIT", fg="red",
                         command=frame.quit)
    self.button.pack(side=LEFT, pady = 35,  padx = 10)
    #On Pressing Enter
    #root.bind('<Return>',lambda root = root, username = username , password = password: self.call_script(root, username, password))
    root.bind("<Return>", lambda event: self.clickButton(event))

  def validate_cert(self, certificate):
      if (certificate[0:27] == constants.CERT_START) and (certificate[-26:].strip() == constants.CERT_END):
        return True
      else:
        return False  

  def clickButton(self, event):
    try:
        widget = root.focus_get()
        if widget != root:
            widget.invoke()
    except Exception:
        #Catch exception for widgets not having invoke() method and do nothing
        pass
        #self.message2.configure(text= constants.GENERAL_ERROR_MSG)          

  def call_script(self, root, username, password):
    try:
      #Disable all the buttons
      self.button.config(state='disabled')
      self.slogan.config(state='disabled')
      #Resetting messages
      self.message2['text'] = ""
      self.message3['text'] = ""
      self.message2['fg'] = 'blue'
      self.message3['fg'] = 'blue'
      #Perform the task
      data=fetch.main()
      #data = ['940773', '-----BEGIN CERTIFICATE-----\nsdasdasdasda\n-----END CERTIFICATE-----']
      if len(data) == 2:
        if data[0] == constants.FAILURE_MSG_FROM_FETCH or data[1] == constants.FAILURE_MSG_FROM_FETCH:
          self.message2['text'] = constants.CERT_FETCH_FAILURE_MSG
          self.message2['fg'] = 'red'
        else:
          #Checking format of certificate
          cert_validation = False
          cert_validation = self.validate_cert(data[1])
          if cert_validation is True:
            self.message2['text'] = constants.CERT_FETCH_SUCCESS_MSG + data[0]
            self.message3['text'] = constants.CERT_UPDATE_IN_PROGESS
            self.message3['fg'] = 'black'
            #Call Symportal REST API for updating Certificate
            url= constants.URL_UPDATE_CERT + data[0]
            payload = {'certificate' : data[1]}
            response=requests.put(url, auth=(username, password), data = payload, verify=False)
            if response.status_code == 200:
              self.message3['text'] = constants.CERT_UPDATE_SUCCESS_MSG
              self.message3['fg'] = 'blue'
            else:
              self.message3['text'] = constants.CERT_UPDATE_FAILURE_MSG                
              self.message3['fg'] = 'red'
          else:
            self.message2['text'] = constants.CERT_INVALID_MSG 
            self.message2['fg'] = 'red'
            self.message3['text'] = constants.CERT_UPDATE_FAILURE_MSG
            self.message3['fg'] = 'red'
      else:
        self.message2['text'] = constants.CERT_FETCH_FAILURE_MSG
        self.message2['fg'] = 'red'
      #Enable all the buttons
      self.button.config(state='active')
      self.slogan.config(state='active')
    except Exception as e:
      self.message2['text'] = constants.GENERAL_ERROR_MSG
      self.message3['text'] = ""

#def main(username, password):
root = Tk()
root.wm_title("Modem Provisioing APP")
#For removing maximize button
root.resizable(0,0)
w = 500 # width for the Tk root
h = 250 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
username = sys.argv[1]
password = sys.argv[2]
app = App(root, username, password)
root.mainloop()
