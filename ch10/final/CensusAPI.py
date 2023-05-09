import requests
import json 
class CensusAPI:
    def __init__(self):
        """initilialize the url with api key
        args:none 
        return :none"""
        self.api_url = "https://api.census.gov/data/2019/pep/charagegroups?get=NAME,POP&HISP=2&for=state:*&key=cd7a10f30f60e7c1bb0ba39c7564dc5426a123b8"
        self.hispanicpopulation = {}
    

    def get(self):
        json_file = requests.get(self.api_url).json()
        for _ in json_file[1:]:
            state = _[0]
            population = int(_[1])
            self.hispanicpopulation[state] = population
        most_hispanic_state = max(self.hispanicpopulation, key = self.hispanicpopulation.get) 
        least_hispanic_state = min(self.hispanicpopulation, key = self.hispanicpopulation.get) 
        print( "The most hispanic state is," + most_hispanic_state)
        print( "The least hispanic state is," + least_hispanic_state)