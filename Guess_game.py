import random
def guess(x):
    Random_number=random.randint(1,x)
    guess=0
    while guess != Random_number:
        guess=int(input(f"Guess a number 1 and {x}:-  "))
        if guess>Random_number:
            print(f"{user}Your guess is high:- ")
        elif guess<Random_number:
            print(f"{user}Your guess is Too low:- ")
    print(f"Cnograts!{user} you are guess the correct number:- ")
user=input("Please! enter your name")
aa=int(input("Enter the number of range you want to guess:-  "))
guess(aa)
