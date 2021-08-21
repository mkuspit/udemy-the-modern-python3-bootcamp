from random import shuffle

class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit
		
	def __repr__(self):
		return f"{self.value} of {self.suit}"



class Deck:
	def __init__(self):
		suits = ("Hearts", "Diamonds", "Clubs", "Spades")
		values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
		self.cards = [Card(v, s) for s in suits for v in values]


	def __repr__(self):
		return f"Deck of {self.count()} cards"


	def _deal(self, num):
		count = self.count()
		c = min([count, num])
		if count == 0:
			raise ValueError("All cards have been dealt")
		cards = self.cards[-actual:]
		self.cards = self.cards[:-actual]
		return cards


	def shuffle(self):
		if self.count() < 52:
			raise ValueError("Only full decks can be shuffled")
		shuffle(self.cards)
		return self


	def deal_card(self):
		return self._deal(1)[0]


	def deal_hand(self, hand_size):
		return self._deal(hand_size)


	def count(self):
		return len(self.cards)