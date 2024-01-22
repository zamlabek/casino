# game_logic.py

def play_round(bet_slot, winning_slot, bet_amount, my_money):
    if bet_slot == winning_slot:
        print(f"Congratulations! You won ${bet_amount * 2}!")
        my_money += bet_amount * 2
    else:
        print(f"Sorry, you lost ${bet_amount}. Better luck next time.")
        my_money -= bet_amount

    return my_money

def calculate_result(my_money):
    print(f"Game over. Your final balance is ${my_money}")
    if my_money > int(config("MY_MONEY")):
        print("Congratulations! You're a winner.")
    elif my_money == int(config("MY_MONEY")):
        print("You broke even.")
    else:
        print("Unfortunately, you lost.")

