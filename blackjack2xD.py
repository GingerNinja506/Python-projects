import random
def blacjack():
    game_end = False
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n'\n")
    if play_game == "y":
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        user_hand = []
        computer_hand = []    
        user_hand.append(random.choice(cards))
        user_hand.append(random.choice(cards))
        computer_hand.append(random.choice(cards))
        computer_hand.append(random.choice(cards))
        scores ={
        "user": sum(user_hand),
        "computer": sum(computer_hand),
        }
        if scores["user"] == 21:
            print("You Win")
        else:
            print(f"Your cards {user_hand}, current score: {scores['user']}")
            print(f"Computer firts card {computer_hand[0]}")
        while scores["user"] and scores["computer"] < 21:
                def drawing_card():
                    user_input = input("Type 'y' to get another card, type 'n' to pass:\n")
                    if user_input == "y":
                        new_card = random.choice(cards)
                        user_hand.append(new_card)
                        scores["user"] += new_card
                        if 11 in user_hand and sum(user_hand) > 21:
                            user_hand.remove(11)
                            user_hand.append(1)
                        if 11 in computer_hand and sum(computer_hand) > 21:
                            computer_hand.remove(11)
                            computer_hand.append(1)                
                        print(f"Your cards {user_hand}, current score: {scores['user']}")
                        print(f"Computer firts card {computer_hand[0]}")
                        if scores["user"] == 21:
                            print("You Win")
                        elif scores["user"] > 21:
                            print("You went over 21 you lose GAME OVER")
                            game_end = True
                    elif user_input == "n":
                        if sum(computer_hand) < 17:
                            new_card = random.choice(cards)
                            computer_hand.append(new_card)
                            scores["computer"] += computer_hand[-1]
                        print(f"Your final hand {user_hand}, final score: {scores['user']}")
                        print(f"Computer final hand {computer_hand}, final score: {scores['computer']}")
                        if scores['computer'] > 21:
                            print("Opponent went over you win")
                            game_end = True
                        elif scores["computer"] > scores["user"]:
                            game_end = True
                            print("Computer have bigger hand you lose")
                        elif scores['computer'] < scores['user']:
                            game_end = True
                            print("You have bigger hand than computer, you win!")
                        else:
                            game_end = True
                            print("You have same scores with computer it's DRAW")
                            
                drawing_card()
blacjack()
            

