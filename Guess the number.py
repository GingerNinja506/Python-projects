import random
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess the number from 1 to {x}  "))
        if guess < random_number:
            print("Number is to low")
        elif guess > random_number:
            print("Sorry number is to high")
        else:
            print("Yay u made it")
guess(10)
    
    
        


