from tkinter import * # importing tkinter

root = Tk()

def search():
    realanime = anime.get()
    print(realanime)

#making an anime varible 
anime = StringVar()
#setting up window
root.title("OgOaNiMe") #Nameing window title
root.configure(background='#303030') # Making backround black
root.geometry('1920x1080') # Setting default window size to 1920x1080
# adding a search bar 
E1 = Entry(root, bd=0, exportselection=0, width=100, textvariable=anime).pack() # display on root, no borders, backround yellow, do not copy to clipboard, width of 10 are its prameters
B1 = Button(root,text="Search",command=search).pack() # Display on root and if clicked run search function

root.mainloop()
#Import main.py so I can use Search in main file