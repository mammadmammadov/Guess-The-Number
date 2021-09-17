from random import randint
first=1
last=100
randomNumber=randint(first, last)
print(f"The computer generated a random integer between {first} and {last}.")
guess=None
while randomNumber!=guess:
    guess=int(input("What is your guess?: "))
    if guess>randomNumber:
        print("It is higher! Decrease it!")
    elif randomNumber>guess:
        print("It is lower! Increase it!")
    else:
        print("Congratulations, you won the game!")