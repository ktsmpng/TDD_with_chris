class Movies:

	def __init__(self, customer):
		self.customer = customer
		self._statement = 'Rental Record For {} \n{}You owe {} \nYou earned {}'
		self.rented_movies = {}
		self.catalog = {'Crazynotes': 'Regular',
						'Teeth': 'Regular',
						'The Web': 'Regular',
						'Spongebob': 'Child',
						'Avengers': 'New Release',}

	def get_statement(self):
		try:
			self._statement = self._statement.format(self.customer, self.movies_with_price(), self.calculate_total(), self.calculate_points())
		except:
			self._statement = self._statement.format(self.customer, '')

		return self._statement

	def add_rental(self, **movies):
		for movie, rented_days in movies.items():
			self.rented_movies[movie] = rented_days

	def rented_days(self, movie):
		return self.rented_movies[movie]

	def movies_with_price(self):
		rented_movies = ''
		for movie in self.rented_movies:
			if self.catalog[movie] == 'Regular':
				rented_movies += f' {movie} {self.calculate_regular_movie_price(movie)} \n'
			elif self.catalog[movie] == 'Child':
				rented_movies += f' {movie} {self.calculate_childs_movie_price(movie)} \n'
			elif self.catalog[movie] == 'New Release':
				rented_movies += f' {movie} {self.calculate_new_release_movie_price(movie)} \n'
		return rented_movies

	def calculate_regular_movie_price(self, movie):
		additional_days_price = (1.5 * (self.rented_days(movie) - 2))
		price = 2.0 + additional_days_price if self.rented_days(movie) > 2 else 2.0 
		return price

	def calculate_childs_movie_price(self, movie):
		additional_days_price = (1.5 * (self.rented_days(movie) - 3))
		price = 1.5 + additional_days_price if self.rented_days(movie) > 3 else 1.5
		return price

	def calculate_new_release_movie_price(self, movie):
		price = 3.0 * self.rented_days(movie)
		return price

	def calculate_total(self):
		total = 0.0
		for movie in self.rented_movies:
			if self.catalog[movie] == 'Regular':
				total += self.calculate_regular_movie_price(movie)
			elif self.catalog[movie] == 'Child':
				total += self.calculate_childs_movie_price(movie)
			elif self.catalog[movie] == 'New Release':
				total += self.calculate_new_release_movie_price(movie)
		return total

	def calculate_points(self):
		total = 0
		for movie in self.rented_movies:
			if self.catalog[movie] == 'Regular':
				total += 1
			elif self.catalog[movie] == 'Child':
				total += 1
			elif self.catalog[movie] == 'New Release':
				total += self.calculate_new_release_movie_points(movie)
		return total

	def calculate_new_release_movie_points(self, movie):
		return 1 if self.rented_days(movie) == 1 else 2




