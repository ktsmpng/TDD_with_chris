class Movies:

	def __init__(self, customer):
		self.customer = customer
		self._statement = 'Rental Record For {} \n{}You owe 0.0 \nYou earned 0'
		self.rented_movies = []

	def get_statement(self):
		rented_movies = ''
		for movie in self.rented_movies:
			rented_movies += f' {movie} \n'
		try:
			self._statement = self._statement.format(self.customer, rented_movies)
		except:
			self._statement = self._statement.format(self.customer, '')

		print(self._statement)
		return self._statement

	def add_rental(self, *movies):
		for movie in movies:
			self.rented_movies.append(movie)
