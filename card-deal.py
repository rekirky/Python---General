import random

class Deck():
  def __init__(self):
    SUITE = 'H D S C'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    self.allcards = [(s, r) for s in SUITE for r in RANKS]

  def shuffle(self):
    random.shuffle(self.allcards)
    print("\nSHUFFLED CARDS\n")
    print(self.allcards)
    print("\n")
    return self.allcards

  def deal_card(self):
    return self.allcards.pop(0)

deck = Deck()
deck.shuffle()

hands = [[],[]]

for player_hand in range(4):
  hands[player_hand % 2].extend([deck.deal_card()])
  print(hands)