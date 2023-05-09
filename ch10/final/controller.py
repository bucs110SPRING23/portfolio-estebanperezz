import csv 
import requests
import tkinter
from CensusAPI import CensusAPI
from tmdb import Tmbd
class Controller:
    def mainloop(self):
        c = CensusAPI() 
        check =c.get()
        print(check)
        t = Tmbd()
        t.mainwindow(self) 
        



        