class Movies:

	def __init__(self, customer):
		self.customer = customer
		self._statement = 'Rental Record For {} \n{}You owe 0.0 \nYou earned 0'
		self.rented_movies = []
		self.catalog = {'Crazynotes': 'Regular',
						'Teeth': 'Regular',
						'The Web': 'Regular',
						'Spongebob': 'Child',
						'Avengers': 'New Release',}

	def get_statement(self):
		try:
			self._statement = self._statement.format(self.customer, self.movies_with_price())
		except:
			self._statement = self._statement.format(self.customer, '')

		return self._statement

	def add_rental(self, *movies):
		for movie in movies:
			self.rented_movies.append(movie)

	def movies_with_price(self):
		rented_movies = ''
		for movie in self.rented_movies:
			if self.catalog[movie] == 'Regular':
				rented_movies += f' {movie} 2.0 \n'
			elif self.catalog[movie] == 'Child':
				rented_movies += f' {movie} 1.5 \n'
			elif self.catalog[movie] == 'New Release':
				rented_movies += f' {movie} 3.0 \n'
		return rented_movies


