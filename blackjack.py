import random

# creat deck
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = [(rank, suit) for suit in suits for rank in ranks]

# CACULATE
def calculate_score(hand):
    score = 0
    aces = 0
    for rank, suit in hand:
        if rank in ['J', 'Q', 'K']:
            score += 10
        elif rank == 'A':
            aces += 1
            score += 11
        else:
            score += int(rank)

    while score > 21 and aces:
        score -= 10
        aces -= 1

    return score

# HOLDING CARDS
def display_hand(name, hand, hide_first_card=False):
    if hide_first_card:
        print(f"{name}'s hand: [Hidden], {hand[1]}")
    else:
        print(f"{name}'s hand: {', '.join(f'{r} of {s}' for r, s in hand)} (Score: {calculate_score(hand)})")

# START
def play_blackjack():
    # shuffle
    deck_copy = deck[:]
    random.shuffle(deck_copy)

    player_hand = [deck_copy.pop(), deck_copy.pop()]
    dealer_hand = [deck_copy.pop(), deck_copy.pop()]

    print("\n=== Blackjack Game ===")
    display_hand("Dealer", dealer_hand, hide_first_card=True)
    display_hand("Player", player_hand)

    # player's turn
    while True:
        choice = input("Do you want to [h]it or [s]tand? ")
        if choice == 'h':
            player_hand.append(deck_copy.pop())
            display_hand("Player", player_hand)
            if calculate_score(player_hand) > 21:
                print("Bust! You lose.")
                return
        elif choice == 's':
            break
        else:
            print("Invalid choice. Please type h or s. Did you type any blank?")

    # dealer's turn
    print("\nDealer's turn:")
    display_hand("Dealer", dealer_hand)
    while calculate_score(dealer_hand) < 17:
        print("Dealer hits.")
        dealer_hand.append(deck_copy.pop())
        display_hand("Dealer", dealer_hand)

    dealer_score = calculate_score(dealer_hand)
    player_score = calculate_score(player_hand)

    # print the result
    print("\n=== Result ===")
    if dealer_score > 21:
        print("Dealer busts! You win!")
    elif dealer_score > player_score:
        print("Dealer wins.")
    elif dealer_score < player_score:
        print("You win!")
    else:
        print("It's a tie!")



if __name__ == "__main__":
    while True:
        play_blackjack()
        again = input("\nPlay again? (y/n): ")
        if again != 'y':
            print("Thanks for playing!")
            break