from random import randint
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5

print("welcome to the number guessing game ")
print("am thinking of a number between 1 to 100.")
answer=randint(1,100)
print("1.easy")
print("2.hard")
choice=int(input("enter your choice:"))
def check_answer(user_answer,actual_answer,turns):
    if user_answer>actual_answer:
        print("too high")
        return turns-1
    elif user_answer<actual_answer:
        print("too low")
        return turns-1
    else:
        print(f"you got it")
def game():
    def set_difficulty():
        if choice==1:
            return EASY_LEVEL_TURNS
        elif choice == 2:
            return HARD_LEVEL_TURNS
        else:
            print("please enter valid choice:")

    turns = set_difficulty()
    guess=0
    while guess!=answer:
        print(f"you have {turns} attempts remaining to guess the number")
        guess=int(input("make a guess:"))
        turns=check_answer(guess,answer,turns)
        if turns==0:
            print("you lose")
            return
        elif guess!=answer:
            print("Guess again")
game()
