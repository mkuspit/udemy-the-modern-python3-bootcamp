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
		act_num = min([count, num])
		

	def shuffle(self):


	def deal_card(self):


	def deal_hand(self, num_cards):


	def count(self):
		return len(self.cards)

