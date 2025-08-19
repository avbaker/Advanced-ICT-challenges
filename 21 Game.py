import random
print(f"Welcome to the classic 21 game!\n\n enter a number to try and get to 21 exactly. you are up against the computer.")

def playerTurn(total, max, player):
    if player:
        print(f"please enter a number between 1 and {max}.")
        choice = int(input(">>> "))
        while choice <1 or choice > max:
            choice = int(input("out of range. Try again>>> "))
    else:
        choice = random.randint(1, max)
        print(f"computer chose {choice}.")
    total += choice

    return total
total = 0
max = 3
p = random.choice([True, False])
while total < 21:
    total = playerTurn(total, max, True if p else False)
    print(f"total: {total}")
    if total == 21:
        print(f"{"player" if p else "computer"} wins!")
    p = not p
