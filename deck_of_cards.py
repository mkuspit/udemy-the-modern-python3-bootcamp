class Card:
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def __repr__(self):
		print(f"{self.value} of {self.suit}")

class Deck:
	def __init__(self):
		self.cards = []
		suits = ("Hearts", "Diamonds", "Clubs", "Spades")
		values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
		for s in suits:
			for v in values:
				self.cards.append(Card(s, v))

	def __repr__(self):
		print(f"Deck of {self.count()} cards")

	def _deal(self):


	def shuffle(self):


	def deal_card(self):


	def deal_hand(self, num_cards):


	def count(self):
		return len(self.cards)

