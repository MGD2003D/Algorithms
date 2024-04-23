@profile
def can_defend(hand_cards, attack_cards, trump):
    ranks = '6789TJQKA'
    hand_cards = sorted([(ranks.index(card[0]), card[1]) for card in hand_cards], key=lambda x: (x[1] != trump, x[0]))
    attack_cards = [(ranks.index(card[0]), card[1]) for card in attack_cards]

    for attack_card in attack_cards:
        defended = False
        for hand_card in hand_cards:
            if hand_card[1] == attack_card[1] and hand_card[0] > attack_card[0] or \
               hand_card[1] == trump and (attack_card[1] != trump or hand_card[0] > attack_card[0]):
                hand_cards.remove(hand_card)
                defended = True
                break
        if not defended:
            return "NO"
    return "YES"

with open('resources/input.txt', 'r') as file:
    n, m, trump = file.readline().split()
    hand_cards = file.readline().split()
    attack_cards = file.readline().split()

result = can_defend(hand_cards, attack_cards, trump)
with open('resources/output.txt', 'w') as file:
    file.write(result)
