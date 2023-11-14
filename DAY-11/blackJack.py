from pickle import TRUE
import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    card = random.choice(cards)
    return card


user_cards = []
computer_cards = []

isGameOver = False


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


for _ in range(2):
    computer_cards.append(deal_card())
    user_cards.append(deal_card())
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)
print(f" Your cards :{user_cards} ,current Score:{user_score}")
print(f"computers first card:{computer_cards[0]}")

if user_score == 0 or computer_score == 0 or user_score > 21:
    isGameOver = True
