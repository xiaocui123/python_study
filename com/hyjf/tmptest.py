import collections
from random import choice

Card=collections.namedtuple("Card",'rank suit')

class FrenchDeck:

    ranks=[str(n) for n in range(2,11)]+list('JQKA')

    suits="spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank,suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


suit_values=dict(spades=3,hearts=2,diamonds=1,clubs=0)

def spades_high(card):
    rank_value=FrenchDeck.ranks.index(card.rank)
    return  rank_value*len(suit_values)+suit_values[card.suit]


if __name__ == '__main__':

    deck = FrenchDeck()

    print(len(deck))

    print(deck[0])

    print(deck[-1])

    print([deckk for deckk in deck])

    print(choice(deck))

    for card in sorted(deck,key=spades_high):
        print(card)

    a,b,*rest=range(5)
    print(a,b,rest)

    l=list(range(10))
    print(l)

    print(l[2:5])
