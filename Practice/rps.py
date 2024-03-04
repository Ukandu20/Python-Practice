import random

def generate_card():
    card = []
    for _ in range(5):
        column = random.sample(range(1, 16), 5)
        card.append(column)
    card[2][2] = 'FREE'  # Mark the center cell as 'FREE'
    return card

def display_card(card):
    print("BINGO CARD")
    print("----------")
    for row in card:
        print('\t'.join(str(num) for num in row))
    print()

def mark_number(card, number):
    for row in card:
        if number in row:
            row[row.index(number)] = 'X'

def is_winner(card):
    # Check rows
    for row in card:
        if all(num == 'X' for num in row):
            return True
    
    # Check columns
    for col in range(5):
        if all(card[row][col] == 'X' for row in range(5)):
            return True

    # Check diagonals
    if all(card[i][i] == 'X' for i in range(5)) or \
       all(card[i][4-i] == 'X' for i in range(5)):
        return True

    return False

def play_bingo():
    print("Welcome to Bingo!")
    print("=================")
    player_card = generate_card()
    computer_card = generate_card()

    print("\nYour Card:")
    display_card(player_card)

    print("Computer's Card:")
    display_card(computer_card)

    numbers_called = set()
    while True:
        if is_winner(player_card):
            print("Congratulations! You won!")
            break
        elif is_winner(computer_card):
            print("Oops! Computer won!")
            break

        number = random.randint(1, 75)
        if number in numbers_called:
            continue

        numbers_called.add(number)
        print(f"\nNumber called: {number}")
        mark_number(player_card, number)
        mark_number(computer_card, number)

        print("\nYour Card:")
        display_card(player_card)

        input("Press Enter to continue...")
        print("\n" * 50)  # Clear the console

play_bingo()
