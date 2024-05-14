from random import randint

def get_dices() -> list:
    return [randint(1, 6), randint(1, 6)]

def get_dices_sum(dices: list) -> None:
    print(f"The sum of the dice is {dices[0]} + {dices[1]} = {sum(dices)}")

def check_input(user_input) -> bool:
    if user_input not in ['0', '1', 'exit', 'start']:
        print("Invalid input! Please enter '0', '1', 'exit', or 'start'.")
        return False
    return True