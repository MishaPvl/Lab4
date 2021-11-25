from lab1 import * 
def encrypt(deck, key, p):
    return [pow(card, key, p) for card in deck]

def cards_to_str(cards):
    return [cards[card - 2] for card in cards]

players = int(input("Введите кол-во игроков: "))
card_suits = ['Diamond', 'Hearth', 'Spades', 'Clubs']
card_numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
cards_deck = []
for i in card_suits:
    for j in card_numbers:
        cards_deck.append(str(i + ' ' + j))

deck = list(range(1, len(cards_deck) + 1))

q = rand_prime(0, 10**9)
p = 2 * q + 1
players_decryption_keys = []

for i in range (players):
    c, d = gen_c_d(p - 1)
    deck = [pow(card, c, p) for card in deck]
    shuffle(deck)
    players_decryption_keys.append(d)

players_cards = [[deck[i], deck[i + 1]] for i in range(0, players * 2, 2)]


for i in range(len(players_cards)):
    for decryption_key in players_decryption_keys:
        players_cards[i] = encrypt(players_cards[i], decryption_key, p)

for i, cards in enumerate(players_cards, 1):
    cards = cards_to_str(cards)
    print(f'Игрок {i} имеет карты', *cards)

