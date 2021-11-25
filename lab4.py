from lab1 import *

players_count = int(input('Введите число игроков: '))

if players_count > 23:
    print("Не может быть больше 22 игроков")
    exit(1)
card_power =  ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
card_suit = ['Diamond', 'Hearth', 'Spades', 'Clubs']
temp_deck = []
for i in card_suit:
    for j in card_power:
        temp_deck.append(str(i + ' ' + j))
full_deck = temp_deck


def encrypt(deck, key, p):
    return [pow(card, key, p) for card in deck]


def card_view(cards):
    return [full_deck[card - 1] for card in cards]



deck = list(range(1, len(full_deck) + 1))
assert len(deck) == 52

p = rand_prime(1, 10**9)

players_decryption_keys = []
for _ in range(players_count):
    player_c, player_d = gen_c_d(p - 1)
    deck = encrypt(deck, player_c, p)  
    shuffle(deck)
    players_decryption_keys.append(player_d)

players_cards = [[deck[i], deck[i + 1]] for i in range(0, players_count * 2, 2)]
table_card = [deck[i] for i in range(players_count * 2, len(deck))]
print(table_card)
print(players_cards)
print('\n')


for d in players_decryption_keys:
    table_card = encrypt(table_card, d, p)

for i in range(len(players_cards)):
    for d in players_decryption_keys:
        players_cards[i] = encrypt(players_cards[i], d, p)
print(table_card)
print(players_cards)
print('\n')

for i, cards in enumerate(players_cards, 1):
    cards = card_view(cards)
    print(f'Игрок {i} имеет карты', cards)
    
table_desk = []
for i in table_card:
   table_desk.append(full_deck[i - 1])
print(f'Карты на столе: {table_desk}')
