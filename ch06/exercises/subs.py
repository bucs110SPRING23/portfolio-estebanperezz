import json 
def main():
    text= open("news.txt","r").read().lower()
    sub_fptr = open("subs.json","r")
    subs = json.load(sub_fptr)
    print(subs,type(subs))
    for k, v in subs.items():
        text = text.replace(k,v)
    fptr = open("Betternews.txt","w")
    fptr.write(text)
    fptr.close()
main()
