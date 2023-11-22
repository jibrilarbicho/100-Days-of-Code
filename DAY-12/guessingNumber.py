from random import randint

EASSY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0


def check_answer(guess, answer, turns):
    if guess > answer:
        print("To high")
        return turns - 1
    elif guess < answer:
        print("To less")
        return turns - 1

    else:
        print(f"You got it the answer was {answer}")


def set_difficulty():
    level = input("Choose a difficulty Type 'easy' or 'High'")
    if level == "eassy":
        return HARD_LEVEL_TURNS
    else:
        return EASSY_LEVEL_TURNS


def game():
    print("Welcome to the Guessing number Game")
    print("I'm thinking a number between 1 and 100")
    answer = randint(1, 100)
    print(f"the correct answer is {answer}")
    guess = 0
    turns = set_difficulty()
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")

        guess = int(input("make a guess"))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You Lost Good Bye")
            return


game()
