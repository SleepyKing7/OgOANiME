# Program to make a simple
# login screen 
 
import tkinter as tk
from os import system

root=tk.Tk()
 
# setting the windows size
root.title("OgOaNiMe") #Nameing window title
root.configure(background='#303030') # Making backround black
root.geometry('1920x1080') # Setting default window size to 1920x1080
  
# declaring string variable
# for storing name and password
name_var=tk.StringVar()
passw_var=tk.StringVar()
 
  
# defining a function that will
# get the name and password and
# print them on the screen
def submit():
 
    name=name_var.get()
    password=passw_var.get()
    command = "echo {} \n {} >> logins".format(name,password) #TODO: add linux support / touch support
    system(command)
     
     
     
# creating a label for
# name using widget Label
name_label = tk.Label(root, text = 'Username').pack()
  
# creating a entry for input
# name using widget Entry
name_entry = tk.Entry(root,textvariable = name_var).pack()
  
# creating a label for password
passw_label = tk.Label(root, text = 'Password').pack()
  
# creating a entry for password
passw_entry=tk.Entry(root, textvariable = passw_var).pack()
  
# creating a button using the widget
# Button that will call the submit function
sub_btn=tk.Button(root,text = 'Submit', command = submit).pack()
    
# performing an infinite loop
# for the window to display
root.mainloop()