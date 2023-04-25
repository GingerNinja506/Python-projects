import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
guess = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))
if guess == 0:
 print(rock)
elif guess == 1:
 print(paper)
elif guess == 2:
 print(scissors)
else:
 print("You cheated You lose!")
 
if int(guess) >= 0 and int(guess) <=2 :
 print("Computer choose:")

random_number = random.randint(0,2)
if int(guess) >= 0 and int(guess) <=2 :
  if random_number == 0:
   print(rock)
  elif random_number ==1:
   print(paper)
  else:
   print(scissors)

if int(guess) >= 0 and int(guess) <=2 :
 if guess == random_number:
  print("Draw")
 elif int(guess) > random_number:
  print("You Win!")
 else:
  print("Compute Wins!")





