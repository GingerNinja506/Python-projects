#100 days of code challange day 2

# You are going to write a program that tests the compatibility between two people.
#To work out the love score between two people:
#Take both people's names and check for the number of times the letters in the word TRUE occurs. 
#Then check for the number of times the letters in the word LOVE occurs. 
#Then combine these numbers to make a 2 digit number.
# And then it's just printing some love calculation strings depending on the score 
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_names = (name1.lower() + name2.lower())
true_number = combined_names.count("t") + combined_names.count("r") + combined_names.count("u") + combined_names.count("e")
love_number = combined_names.count("l") + combined_names.count("o") + combined_names.count("v") + combined_names.count("e")

love_and_true_number = str(true_number) + str(love_number) 
if int(love_and_true_number) < 10 or int(love_and_true_number) > 90:
    print(f"Your score is {love_and_true_number}, you go together like coke and mentos")
elif int(love_and_true_number) > 40 and int(love_and_true_number) < 50:
    print(f"Your score is {love_and_true_number}, you are alright together")
else:
    print(f"Your score is {love_and_true_number}.")

