def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return n

# Tests

def test_fizzbuzz():
    assert fizzbuzz(15) == 'FizzBuzz'
    assert fizzbuzz(45) == 'FizzBuzz'

def test_fizz():
    assert fizzbuzz(3) == 'Fizz'
    assert fizzbuzz(6) == 'Fizz'
    assert fizzbuzz(21) == 'Fizz'

def test_buzz():
    assert fizzbuzz(5) == 'Buzz'
    assert fizzbuzz(35) == 'Buzz'
    assert fizzbuzz(50) == 'Buzz'

def test_nonfizzbuzz():
    assert fizzbuzz(7) == 7
    assert fizzbuzz(11) == 11
    assert fizzbuzz(38) == 38
