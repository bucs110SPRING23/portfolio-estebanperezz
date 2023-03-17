numStars = int(input("How many rows of stars"))

def numofStars(i):
    for i in range(1,numStars+1):
        print("*" * i)
numofStars(numStars)