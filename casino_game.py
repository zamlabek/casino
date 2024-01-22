import random
from decouple import config
from game_logic import play_round, calculate_result


def main():
    my_money = int(config("MY_MONEY", default=1000))
    bet_range = list(range(1, 11))

    while True:
        print(f"Your current balance: ${my_money}")
        bet_slot = int(input("Choose a slot to place your bet (1-10): "))

        if bet_slot not in bet_range:
            print("Invalid slot. Please choose a number between 1 and 10.")
            continue

        bet_amount = int(input("Enter your bet amount: "))
        if bet_amount > my_money:
            print("You don't have enough money. Try again.")
            continue

        winning_slot = random.choice(bet_range)
        print(f"Winning slot: {winning_slot}")

        my_money = play_round(bet_slot, winning_slot, bet_amount, my_money)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    calculate_result(my_money)

if __name__ == "__main__":
    main()
