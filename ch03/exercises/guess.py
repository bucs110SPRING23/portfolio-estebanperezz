import random 
randomnumber = random.randrange(1,11)
tries = 0
for tries in range(0,3):
    guess = int(input("Enter a number 1-10"))
    if guess != randomnumber:
        if guess>randomnumber:
            print("too high guess")
            tries +=1 
        elif guess<randomnumber:
            print("guess too low")
            tries +=1
    elif guess ==randomnumber:
        "You are correct"
        break


