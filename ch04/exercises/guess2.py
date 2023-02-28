#collection objects 
#Strings - list of chars immutable 
#Lists - list of any set of objects - mutable 
#Tuples - immutable list of any set of objects 
#mytuble= (5,8,1,.1)
#Dictionaries -- used to store--key value pairs
##mydict {"a":1,b:2,c:3}
#Dictionaries
##Guessing 
import random 
randomnumber = random.randrange(1,1000)
print(randomnumber)
guessBool = True
numGuess = 0 
randomGuess = int(input("Enter a random guess"))
while guessBool :
    randomGuess = int(input("Enter a random guess"))
    numGuess +=1 
    print(randomGuess)
    print(numGuess)
    if guessBool == randomGuess:
        guessBool = False
    
        print(numGuess)
#Some while loops cant be recreated with for loops 
print("Enter numbers to sum['q' to quit]")
while sum!='q':
    value = input("number: ")
    if value.is_digit():
        value = int(value)
        sum+= value
    elif value =='q':
        print("Enter numbers to sum['q'] to quit")
while True:
    value= input("number: ")
    if value.isdigit():
        value = int(value)
        sum+=value
    elif value =='q':
        print("Enter numbers to sum['q'] to quit")
        