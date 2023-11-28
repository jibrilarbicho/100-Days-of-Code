from operator import truediv
from tabnanny import check
from turtle import clear
from art import logo, vs
from game_data import data
import random

print(logo)
account_b = random.choice(data)

score = 0

game_should_continue = True
while game_should_continue:

    def format_data(account):
        account_descr = account["description"]
        account_name = account["name"]
        account_country = account["country"]
        return f"{account_name},a {account_descr},from {account_country}"

    def check_answer(guess, a_followeres, b_followers):
        if a_followeres > b_followers:
            return guess == "a"
        else:
            return guess == "b"

    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)
    print(f"Compare A:{format_data(account_a)}.")
    print(vs)
    print(f"Against B:{format_data(account_b)}.")
    guess = input("Who has more Followesrs Type 'A' or 'B'").lower()
    a_follwer_count = account_a["follower_count"]
    b_follwer_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follwer_count, b_follwer_count)
    if is_correct:
        score += 1
        print("You are Right")
    else:
        game_should_continue = False
        print(f"Sorry, that's Wrong. Final Score: {score}")
