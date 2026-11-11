from random import shuffle
from os import system
from time import sleep

def create_deck():
	return (list("A23456789JQK") + ["10"]) * 4

def pull_card(deck):
	return deck.pop()

def get_hand_string(hand):
	return "|" + "||".join(hand) + "|"

def get_hit_stand():
	while True:
		user_input = input("Hit (H) or Stand (S)? ")

		if user_input in ("H", "S"):
			return user_input

def get_value(hand):
	value = 0
	aces = 0

	for card in hand:
		if card.isdigit():
			value += int(card)
		elif card == "A":
			aces += 1
		else:
			value += 10

	for _ in range(aces):
		value += 1 if value + 11 > 21 else 11

	return value

while True:
	deck = create_deck()
	shuffle(deck)

	hand = [pull_card(deck), pull_card(deck)]
	dealer_hand = [pull_card(deck)]

	system("clear")
	print("Your Hand: " + get_hand_string(hand))
	print("Dealer's Hand: " + get_hand_string(dealer_hand + ["X"]))

	is_game_over = False

	while True:
		user_input = get_hit_stand()

		if user_input == "H":
			hand.append(pull_card(deck))
			print("Your Hand: " + get_hand_string(hand))

			if get_value(hand) > 21:
				is_game_over = True
				break
		else:
			print("Your Hand: " + get_hand_string(hand))
			break

	if is_game_over:
		print("Bust! Dealer Won!")

		if input('Type "Exit" to stop game: ') == "Exit":
			break
	else:
		dealer_hand.append(pull_card(deck))
		print("Dealer's Hand: " + get_hand_string(dealer_hand))

		while True:
			print("Hit (H) or Stand (S)? ", end="", flush=True)
			sleep(2)

			if get_value(dealer_hand) <= get_value(hand):
				print("H")
				dealer_hand.append(pull_card(deck))
				print("Dealer's Hand: " + get_hand_string(dealer_hand))

				if get_value(dealer_hand) > 21:
					break
			else:
				print("S")
				print("Dealer's Hand: " + get_hand_string(dealer_hand))
				break

		if get_value(dealer_hand) > 21:
			print("Bust! You Won!")
		elif get_value(dealer_hand) > get_value(hand):
			print("Dealer Won!")
		elif get_value(hand) > get_value(dealer_hand):
			print("You Won!")
		else:
			print("Tie!")

		if input('Type "Exit" to stop game: ') == "Exit":
			break
