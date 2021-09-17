from random import randint
start=1
end=10
value=randint(start, end)
print(f"The computer chooses a number between {start} and {end}.")
guess=None
while value!=guess:
    guess=int(input("Guess the number: "))
    if guess>value:
        print("Your number is higher!")
    elif value>guess:
        print("Your number is lower!")
    else:
        print("COngratulations! You won the game!")