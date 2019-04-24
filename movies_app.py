class Movies:
	_statement = f"Rental Record For {self.customer} \n You Owe 0.0 \n You earned 0"

	def __init__(self, customer):
		self.customer = customer

	def statement(self):
		return _statement