import pytest 
import fizzbuzz

def test_three():
    assert fizzbuzz.fizzbuzz(3) == "Fizz"
    
def test_two():
    assert fizzbuzz.fizzbuzz(15) == "FizzBuzz"    
    
def test_five():
    assert fizzbuzz.fizzbuzz(5) == "Buzz"       
     
def test_six():
    assert fizzbuzz.fizzbuzz(17) == "17"         