#json - string format not file formats \
import json
def main():
    file_pointer = open("assets.txt","a")
    idea = input("Enter an idea")
    data = json.load(file_pointer)
    data.append

json_data = {
    "title":"The Matrix",
    "msg":"Hello World"

}
json_string = json.dumps(json_data)
print(json_string,type(json_string))
for k , v in json_data.items():
    print(k,v)
fptr = open("asset.json","w")
fptr.write(json_string)
fptr.close() 
data_str = open("assets.txt","r").read()
data = json.loads(open("assets.txt","r").read())
fptr.close()
print(data,type(data))