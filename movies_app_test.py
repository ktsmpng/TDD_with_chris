from movies_app import Movies

def test_return_blank_statement():
	movie = Movies("Jim Bob")
	assert movie.get_statement() == "Rental Record For Jim Bob \n You Owe 0.0 \n You earned 0"

def test_return_customer2_statement():
	movie = Movies("Sally Burns")
	assert movie.get_statement() == "Rental Record For Sally Burns \n You Owe 0.0 \n You earned 0"
