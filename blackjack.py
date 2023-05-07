import random
#game_on = True
#want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
#if want_to_play == "n":
   # game_on = False
#else:
    #game_on = True
#while game_on == True:
def blackjack():
        computer_score = 0
        user_score = 0
        while user_score and computer_score <= 21:
            
            
            want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") 
            cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
            user_hand = []
            computer_hand = []    
            user_hand.append(random.choice(cards))
            user_hand.append(random.choice(cards))
            computer_hand.append(random.choice(cards))
            computer_hand.append(random.choice(cards))
            user_score += sum(user_hand)
            computer_first_card = computer_hand[0]
            print(f"Your cards {user_hand}, current score: {user_score}")
            print(f"Computer firts card {computer_first_card}")
            draw_card = input("Do you want to draw another card Type 'y' or 'n': ")
            if draw_card == "y":
                    user_hand.append(random.choice(cards))
                    user_score += user_hand[-1]
            if user_score > 21:
                   print("You went over GAME OVER")
            elif computer_score > 21:
                   print("You win!")
            
            print(f"Your cards {user_hand}, current score: {user_score}")
            print(f"Computer firts card {computer_first_card}")
        
        
blackjack()
    


        
        

