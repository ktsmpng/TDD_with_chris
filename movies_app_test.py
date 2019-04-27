from movies_app import Movies

def test_return_blank_statement():
	movie = Movies("Jim Bob")
	assert movie.get_statement() == "Rental Record For Jim Bob \nYou owe 0.0 \nYou earned 0"

def test_return_customer2_statement():
	movie = Movies("Sally Burns")
	assert movie.get_statement() == "Rental Record For Sally Burns \nYou owe 0.0 \nYou earned 0"

def test_return_customer1_statement_with_movie():
	movie = Movies("Jim Bob")
	movie.add_rental('Crazynotes')
	assert movie.get_statement() == "Rental Record For Jim Bob \n Crazynotes \nYou owe 0.0 \nYou earned 0"
