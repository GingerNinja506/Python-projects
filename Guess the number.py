import random
def game():
    game_on = True
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    lives = 0
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        lives = 10
        print(f"You have {lives} attempts remaining to guess the number.")
    elif level == "hard":
        lives = 5
        print(f"You have {lives} attempts remaining to guess the number.")
    number = random.randint(0,100)
    while game_on == True:
        guess = int(input("Guess a number : "))
    

        if guess != number and guess > number:
                lives -= 1
                print("Too high")
                print("Guess again.")
                print(f"You have {lives} attempts remaining to guess the number.")
        elif guess != number and guess < number:
                lives -= 1
                print("Too low")
                print("Guess again.")
                print(f"You have {lives} attempts remaining to guess the number.")
        elif guess == number:
                print(f"You got it! The answer was {number} ")
                game_on = False

    
game()
    
    
    
    
        


