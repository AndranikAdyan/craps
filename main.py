from functions import *

print("Let's play!")


dices = get_dices()
dices_sum = sum(dices)

if dices_sum == 7 or dices_sum == 11:
	get_dices_sum(dices)
	print("You Won!")
elif dices_sum == 2 or dices_sum == 3 or dices_sum == 12:
	get_dices_sum(dices)
	print("You lose :(")
else:
	get_dices_sum(dices)
	print(f"Now your goal number is {dices_sum}")

	goal_number = dices_sum
	while True:
		dices = get_dices()
		get_dices_sum(dices)
		dices_sum = sum(dices)

		if dices_sum == 7:
			print("You lose :(")
			break
		elif dices_sum == goal_number:
			print("You Won!")
			break