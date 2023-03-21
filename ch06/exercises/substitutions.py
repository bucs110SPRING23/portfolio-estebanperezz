import json
import random 
def readfile():
    with  open("news.txt","r") as file_pointer:
        news = str(file_pointer)
    return news
def subfile():
    with open("subs.json","r") as file_sub:
        try:
            newarticle = json.load(file_sub)
        except json.JSONDecodeError or FileNotFoundError:
            newsarticle = {}
    return newarticle
def main():
    news = readfile()
    newarticle = subfile()
    for key, value in newarticle.items():
        news = news.replace(key,value)
    new_article = open("newnews.txt","w")
    new_article.write(news)
    new_article.close()                  
        #USE OS AUTOMATE LIBRARY IN PYTHON 
main()