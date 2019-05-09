from movies_app import Movies

def test_return_blank_statement():
	movie = Movies("Jim Bob")
	assert movie.get_statement() == "Rental Record For Jim Bob \nYou owe 0.0 \nYou earned 0"

def test_return_customer2_statement():
	movie = Movies("Sally Burns")
	assert movie.get_statement() == "Rental Record For Sally Burns \nYou owe 0.0 \nYou earned 0"

def test_return_list_of_customer_rented_movie():
	movie = Movies("Jim Bob")
	movie.add_rental('Crazynotes')
	assert movie.rented_movies == ['Crazynotes']

def test_return_list_of_customer_rented_movies():
	movie = Movies("Jim Bob")
	movie.add_rental('Crazynotes', 'Teeth')
	assert movie.rented_movies == ['Crazynotes', 'Teeth']

def test_return_customer_statement_with_regular_movie_and_its_price():
	movie = Movies("Jim Bob")
	movie.add_rental('Crazynotes')
	assert movie.get_statement() == "Rental Record For Jim Bob \n Crazynotes 2.0 \nYou owe 0.0 \nYou earned 0"

def test_return_customer_statement_with_regular_and_child_movie_and_its_price():
	movie = Movies("Jim Bob")
	movie.add_rental('Crazynotes', 'Spongebob')
	assert movie.get_statement() == "Rental Record For Jim Bob \n Crazynotes 2.0 \n Spongebob 1.5 \nYou owe 0.0 \nYou earned 0"

def test_return_customer_statement_with_regular_and_child_and_new_movie_and_its_price():
	movie = Movies("Jim Bob")
	movie.add_rental('Crazynotes', 'Spongebob', 'Avengers')
	assert movie.get_statement() == "Rental Record For Jim Bob \n Crazynotes 2.0 \n Spongebob 1.5 \n Avengers 3.0 \nYou owe 0.0 \nYou earned 0"

def test_return_customer_statement_with_regular_for_over_two_days_and_its_price():
	movie = Movies("Jim Bob")
	movie.add_rental('Crazynotes')
	assert movie.get_statement() == "Rental Record For Jim Bob \n Crazynotes 3.5 \nYou owe 0.0 \nYou earned 0"

