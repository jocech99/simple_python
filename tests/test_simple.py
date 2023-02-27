import pytest
from src import simple

"""
Test returns the correct value 
"""
def test_simple_hello():
    assert simple.hello("Jocelyn") == "Hello, Jocelyn", "Shoule return \"Hello, Jocelyn\""

"""
Test anagram OK
"""
def test_is_not_an_anagram():
    assert simple.hello("") ==  "Hello, ",  "Should return \"Hello, \""
