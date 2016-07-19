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
import prov, time, requests

CERT_FETCH_SUCCESS_MSG = "Successfully fetched certificate from modem #"
CERT_FETCH_FAILURE_MSG = "Failed to fetch certificate"
CERT_UPDATE_SUCCESS_MSG = "Successfully updated certificate in the Database"
CERT_UPDATE_FAILURE_MSG = "Failed to update certificate in the Database"
CERT_INVALID_MSG = "Invalid format of Certificate"
CERT_UPDATE_IN_PROGESS = "Updating Certificate in the Database..."
URL="http://localhost:8000/symportal/updatecert/"
CERT_START = "-----BEGIN CERTIFICATE-----"
CERT_END = "-----END CERTIFICATE-----"
FAILURE_MSG_FROM_PROV = "Failed to connect to target!"

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
    self.slogan.pack(side=LEFT, pady = 35)

    self.button = Button(frame, 
                         text="QUIT", fg="red",
                         command=frame.quit)
    self.button.pack(side=LEFT, pady = 35)

  def validate_cert(self, certificate):
      if (certificate[0:27] == CERT_START) and (certificate[-26:].strip() == CERT_END):
        return True
      else:
        return False  

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
      data=prov.main()
      if len(data) == 2:
        if data[0] == FAILURE_MSG_FROM_PROV or data[1] == FAILURE_MSG_FROM_PROV:
          self.message2['text'] = CERT_FETCH_FAILURE_MSG
          self.message2['fg'] = 'red'
        else:
          #Checking format of certificate
          cert_validation = False
          cert_validation = self.validate_cert(data[1])
          if cert_validation is True:
            self.message2['text'] = CERT_FETCH_SUCCESS_MSG + data[0]
            self.message3['text'] = CERT_UPDATE_IN_PROGESS
            self.message3['fg'] = 'black'
            #Call Symportal REST API for updating Certificate
            url= URL + data[0]
            payload = {'certificate' : data[1]}
            response=requests.put(url, auth=(username, password), data = payload, timeout=0.1)
            if response.status_code == 200:
              self.message3['text'] = CERT_UPDATE_SUCCESS_MSG
              self.message3['fg'] = 'blue'
            else:
              self.message3['text'] = CERT_UPDATE_FAILURE_MSG                
              self.message3['fg'] = 'red'
          else:
            self.message2['text'] = CERT_INVALID_MSG 
            self.message2['fg'] = 'red'
            self.message3['text'] = CERT_UPDATE_FAILURE_MSG
            self.message3['fg'] = 'red'
      else:  
        self.message2['text'] = CERT_FETCH_FAILURE_MSG
        self.message2['fg'] = 'red'
      time.sleep(0.2)
      #Enable all the buttons
      self.button.config(state='active')
      self.slogan.config(state='active')
    except Exception:
      root.quit  

def main(username, password):
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
  app = App(root, username, password)
  root.mainloop()