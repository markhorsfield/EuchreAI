class Hand:

	def __init__(self):
		self.cards = []
		self.rects = []

	def get_cards(self):
		return self.cards

	def add_card(self,card):
		self.cards.append(card)

	def set_rects(self,rects):
		self.rects = rects

	def get_rects(self):
		return self.rects

	def remove_rect(self,index):
		print(self.rects)
		for rect,i in zip(self.rects,range(len(self.rects))):
			if i > index:
				self.rects[i-1] = rect
		self.rects.pop(-1)
		print(self.rects)
		
	def remove_card(self,card):
		self.cards.remove(card)

	def set_trump(self,trump_suit):
		for card in self.get_cards():
			if card.get_desc()[0] == trump_suit:
				card.set_trump()

			if trump_suit == 'H':
				left_bower = ['D','J']
			elif trump_suit == 'D':
				left_bower = ['H','J']
			elif trump_suit == 'C':
				left_bower = ['S','J']
			elif trump_suit == 'S':
				left_bower = ['C','J']
			
			if card.get_desc() == left_bower:
				card.set_left()


		