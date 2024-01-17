import random

shuffled_deck = []

deck_of_cards = [
    'Ace of ♠', '2 of ♠', '3 of ♠', '4 of ♠', '5 of ♠',
    '6 of ♠', '7 of ♠', '8 of ♠', '9 of ♠', '10 of ♠',
    'Jack of ♠', 'Queen of ♠', 'King of ♠',
    
    'Ace of ♥', '2 of ♥', '3 of ♥', '4 of ♥', '5 of ♥',
    '6 of ♥', '7 of ♥', '8 of ♥', '9 of ♥', '10 of ♥',
    'Jack of ♥', 'Queen of ♥', 'King of ♥',
    
    'Ace of ♦', '2 of ♦', '3 of ♦', '4 of ♦', '5 of ♦',
    '6 of ♦', '7 of ♦', '8 of ♦', '9 of ♦', '10 of ♦',
    'Jack of ♦', 'Queen of ♦', 'King of ♦',
    
    'Ace of ♣', '2 of ♣', '3 of ♣', '4 of ♣', '5 of ♣',
    '6 of ♣', '7 of ♣', '8 of ♣', '9 of ♣', '10 of ♣',
    'Jack of ♣', 'Queen of ♣', 'King of ♣'
]

def generate_shuffled_deck():
    global shuffled_deck
    i = 0
    while(i < 52):
        random_index = random.randint(0, 51)
        if deck_of_cards[random_index] not in shuffled_deck:
            shuffled_deck.append(deck_of_cards[random_index])
            i += 1


generate_shuffled_deck()


