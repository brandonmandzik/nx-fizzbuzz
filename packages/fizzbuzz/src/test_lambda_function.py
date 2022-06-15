import lambda_function 

def test_validateInput_zero():
    ret = lambda_function.validateInput(0)
    assert ret[1] == 200

def test_validateInput_wrongNumber():
    ret = lambda_function.validateInput(4)
    assert (ret[1] == 400 )

def test_validateInput_fizz():
    ret = lambda_function.validateInput(3)
    assert (ret[1] == 200 and ret[0] == "Fizz" )

def test_validateInput_buzz():
    ret = lambda_function.validateInput(5)
    assert (ret[1] == 200 and ret[0] == "Buzz" )

def test_validateInput_fizzbuzz():
    ret = lambda_function.validateInput(15)
    assert (ret[1] == 200 and ret[0] == "Fizzbuzz" )