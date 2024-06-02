from random import randint

def get_dices() -> list:
    return [randint(1, 6), randint(1, 6)]

def get_dices_sum(dices: list) -> None:
    print(f"The sum of the dice is {dices[0]} + {dices[1]} = {sum(dices)}")