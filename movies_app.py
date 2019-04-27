class Movies:
	_statement = 'Rental Record For {} \n You Owe 0.0 \n You earned 0'

	def __init__(self, customer):
		self.customer = customer

	def get_statement(self):
		return self._statement.format(self.customer)