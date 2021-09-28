# Basic print and get input from keyboard
print("Hello\nPlease enter number")
getNewInput = input()
print("You enter number : ", getNewInput)

# convert data type from string (str) to integer 
print ("Variable getNewInput has data type :", type(getNewInput))
getNewInput = int(getNewInput)
print("\nNew data type of varialbe getNewInput :", type(getNewInput))

# function random 
import random
randomNumber = random.randint(0,100)
print("\nRandom number between 0-100 : ", randomNumber)

# Compare enter number with random number
if randomNumber == getNewInput:
    print("Random number = Input number : ", randomNumber, "=", getNewInput)
else:
    print("Random number != Input number: ", randomNumber, "!=", getNewInput)

#loop to enter number until it equal to random number
while getNewInput != randomNumber:
    getNewInput = input("enter new number to try again :")
    getNewInput = int(getNewInput) #convert
    if  randomNumber == getNewInput:
        print("Yeah!! equal")
        break
    else:
        print("Not equal")