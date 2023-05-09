import csv 
import requests
import tkinter
from CensusAPI import CensusAPI
from tmdb import Tmbd
class Controller:
    def __init__(self):
        
        self.hispanicpopulation = {}
    def mainloop(self):
        c = CensusAPI() 
        c.get() 
        t = Tmbd
        t.mainwindow(self) 
        



        