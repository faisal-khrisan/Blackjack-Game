import random
from art import logo
#start of the program
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#asking the use if he wants to play the game
play =str(input("Would you like to play Blackjack game "
                "Type 'y' for yes and 'n' for no : "))
stop=True
while stop:

    if play.lower()=='y':
        #printing the logo of the program
        print(logo +"\n"*12)
        #creating u ser card list and computer card list
        #def user():
        user_cards = []
        sum_user = 0
        # filling the both user and computer card randomly:
        for n in range(2):
            card_for_user = random.choice(cards)
            user_cards.append(card_for_user)
            sum_user += card_for_user

       # def computer():
        computer_cards = []
        sum_computer = 0
        for n in range(2):
            card_for_computer = random.choice(cards)
            computer_cards.append(card_for_computer)
            sum_computer += card_for_computer

        print(f"The cards in your hand are {user_cards}  and total is : {sum_user}")
        print(f"The Dealer first card {computer_cards[0]}")
        #loop for adding new card
        add_another_card=True
        while add_another_card:
            choice=str(input("type 'y' to add another card and 'n' to pass :"))
            if choice.lower()=='y':
                card_for_user = random.choice(cards)
                user_cards.append(card_for_user)
                sum_user += card_for_user
                print(f"The cards in your hand are {user_cards}  and total is : {sum_user}")
                print(f"The Dealer first card {computer_cards[0]}")
                if sum_user>21:
                    add_another_card=False
                    print(f"The cards in your hand are {user_cards}  and total is : {sum_user}")
                    print(f"The Dealer cards {computer_cards} and total is : {sum_computer}")
                    print("You lost")
                elif sum_user==21 and sum_computer !=21:
                    add_another_card=False
                    print(f"The cards in your hand are {user_cards}  and total is : {sum_user}")
                    print(f"The Dealer cards {computer_cards} and total is : {sum_computer}")
                    print("You win")
                elif sum_user==21 and sum_computer ==21:
                    add_another_card=False
                    print(f"The cards in your hand are {user_cards}  and total is : {sum_user}")
                    print(f"The Dealer cards {computer_cards} and total is : {sum_computer}")
                    print("Game is draw")
            elif choice.lower()=='n':
                while not sum_computer>=17:
                    card_for_computer = random.choice(cards)
                    computer_cards.append(card_for_computer)
                    sum_computer += card_for_computer
                if  (sum_user < sum_computer and sum_computer<=21) or (sum_computer <= 21 and 21 < sum_user):
                    print(f"The cards in your hand are {user_cards}  and total is : {sum_user}")
                    print(f"The Dealer cards {computer_cards} and total is : {sum_computer}")
                    print("You lose")
                    add_another_card = False
                elif sum_user==sum_computer :
                    print(f"The cards in your hand are {user_cards}  and total is : {sum_user}")
                    print(f"The Dealer cards {computer_cards} and total is : {sum_computer}")
                    print("The Game is draw")
                else:
                    print(f"The cards in your hand are {user_cards}  and total is : {sum_user}")
                    print(f"The Dealer cards {computer_cards} and total is : {sum_computer}")
                    print("you won")
                    add_another_card = False

        play = str(input("Would you like to play Blackjack game again 'y' | 'n' : "))
        if play=='y':
            print("\n"*500)
    elif play.lower()=='n':
        stop=False

    else:
        print("Invalid input please try again")
        play = str(input("Would you like to play Blackjack game again 'y' | 'n' : "))
