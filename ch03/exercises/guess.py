import random 
randomnumber = random.randrange(1,11)
print(randomnumber)
tries = 0
for tries in range(0,3):
    guess = int(input("Enter a number 1-10:"))
    if guess != randomnumber:
        if guess>randomnumber:
            print("guess too high")
            tries +=1 
        elif guess<randomnumber:
            print("guess too low")
            tries +=1
    elif guess ==randomnumber:
        print("You are correct")
        break


