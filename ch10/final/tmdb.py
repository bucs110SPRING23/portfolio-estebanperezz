import requests 
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo
import json 

class Tmbd():
    def __init__(self):
        self.url = "http://api.themoviedb.org/3/discover/movie?api_key=2b0268899e7722c303709443c41c21f4&sort_by=popularity.desc&include_adult=true"
        self.titles = []
        self.averagerating = [] 
        
    def mainwindow(self):
        def getallinfo(json_file):
            listbox.delete(0,END)

            for _ in json_file['results']:
                title = _.get('title')
                averagerating = _.get('vote_average')
                self.titles.append(title)
                self.averagerating.append(averagerating)
                listbox.insert(END,f"Title:{title} -->Rating:{averagerating}")
            
        def getoption():
            WatchString = Watchtype.get()
            if Watchtype.get()=="" or Watchtype.get()=="":
                ##If the radio buttons were not selected the user will receive an error message
                messagebox.showerror("Error")
            else:
                json_file =requests.get(f"{self.url}&with_watch_providers={WatchString}").json()
                getallinfo(json_file)

        window = tk.Tk()
        window.title("CS110 Final")
        window.geometry('600x600+40+40')
        
        frame1 = Frame(window)
        frame1.pack(side=TOP)
        
        Watchtype = tk.StringVar() 
        radioNetflix=ttk.Radiobutton(frame1,text="Netflix",value=8, variable=Watchtype)
        radioHulu=ttk.Radiobutton(frame1,text="Hulu",value=15, variable=Watchtype)
        radioPrime=ttk.Radiobutton(frame1,text="Prime",value=9, variable=Watchtype)
        labelStream=tk.Label(frame1,text="Select a Streaming Service", fg="blue", font=(10))
        labelStream.pack(side=LEFT)
        radioNetflix.pack(side=LEFT)
        radioHulu.pack(side=LEFT)
        radioPrime.pack(side=LEFT)
        
        listbox = Listbox(window, height=15, width=30)
        listbox.pack()
        
        buttonget = ttk.Button(window, text="Get options", command=getoption)
        buttonget.pack()
        
        window.mainloop()

T = Tmbd()
T.mainwindow()
