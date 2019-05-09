from movies_app import Movies

def test_return_blank_statement():
	movie = Movies("Jim Bob")
	assert movie.get_statement() == "Rental Record For Jim Bob \nYou owe 0.0 \nYou earned 0"

def test_return_customer2_statement():
	movie = Movies("Sally Burns")
	assert movie.get_statement() == "Rental Record For Sally Burns \nYou owe 0.0 \nYou earned 0"

def test_return_list_of_customer_rented_movie():
	movie = Movies("Jim Bob")
	movie.add_rental(Crazynotes = 1)
	assert movie.rented_movies == {'Crazynotes': 1}

def test_return_list_of_customer_rented_movies():
	movie = Movies("Jim Bob")
	movie.add_rental(Crazynotes = 1, Teeth = 1)
	assert movie.rented_movies == {'Crazynotes': 1, 'Teeth': 1}

def test_return_customer_statement_with_regular_movie_and_its_price():
	movie = Movies("Jim Bob")
	movie.add_rental(Crazynotes = 1)
	assert movie.get_statement() == "Rental Record For Jim Bob \n Crazynotes 2.0 \nYou owe 2.0 \nYou earned 1"

def test_return_customer_statement_with_regular_and_child_movie_and_its_price():
	movie = Movies("Jim Bob")
	movie.add_rental(Crazynotes = 1, Spongebob = 1)
	assert movie.get_statement() == "Rental Record For Jim Bob \n Crazynotes 2.0 \n Spongebob 1.5 \nYou owe 3.5 \nYou earned 2"

def test_return_customer_statement_with_regular_and_child_and_new_movie_and_its_price():
	movie = Movies("Jim Bob")
	movie.add_rental(Crazynotes = 1, Spongebob = 1 , Avengers = 1)
	assert movie.get_statement() == "Rental Record For Jim Bob \n Crazynotes 2.0 \n Spongebob 1.5 \n Avengers 3.0 \nYou owe 6.5 \nYou earned 3"

def test_return_customer_statement_with_regular_for_over_two_days_and_its_price():
	movie = Movies("Jim Bob")
	movie.add_rental(Crazynotes = 2)
	assert movie.get_statement() == "Rental Record For Jim Bob \n Crazynotes 2.0 \nYou owe 2.0 \nYou earned 1"

def test_return_customer_statement_with_regular_for_over_three_days_and_its_price():
	movie = Movies("Jim Bob")
	movie.add_rental(Crazynotes = 3)
	assert movie.get_statement() == "Rental Record For Jim Bob \n Crazynotes 3.5 \nYou owe 3.5 \nYou earned 1"

def test_return_customer_statement_with_childs_movie_and_its_price():
	movie = Movies("Jim Bob")
	movie.add_rental(Spongebob = 1)
	assert movie.get_statement() == "Rental Record For Jim Bob \n Spongebob 1.5 \nYou owe 1.5 \nYou earned 1"

def test_return_customer_statement_with_childs_movie_and_its_price():
	movie = Movies("Jim Bob")
	movie.add_rental(Spongebob = 4)
	assert movie.get_statement() == "Rental Record For Jim Bob \n Spongebob 3.0 \nYou owe 3.0 \nYou earned 1"

def test_return_customer_statement_with_new_release_movie_and_its_price():
	movie = Movies("Jim Bob")
	movie.add_rental(Avengers = 1)
	assert movie.get_statement() == "Rental Record For Jim Bob \n Avengers 3.0 \nYou owe 3.0 \nYou earned 1"


def test_return_customer_statement_with_new_release_movie_and_its_price():
	movie = Movies("Jim Bob")
	movie.add_rental(Avengers = 4)
	assert movie.get_statement() == "Rental Record For Jim Bob \n Avengers 12.0 \nYou owe 12.0 \nYou earned 2"

def test_return_customer_statement_with_new_release_movie_and_its_price():
	movie = Movies("Jim Bob")
	movie.add_rental(Avengers = 4, Spongebob = 8, Crazynotes = 10)
	assert movie.get_statement() == "Rental Record For Jim Bob \n Avengers 12.0 \n Spongebob 9.0 \n Crazynotes 14.0 \nYou owe 35.0 \nYou earned 4"

