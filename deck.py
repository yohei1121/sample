from random import shuffle
from card import Card

class Deck:
    cards = []
    def __init__(self):
        
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))

        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

if __name__ == "__main__":
    deck = Deck()
    for card in deck.cards:
            print(card)
