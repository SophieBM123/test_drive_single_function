from lib.count_words import *
"""
A function called count_words that takes a string as an argument 
and returns the number of words in that string.
"""

"""
Given a string of one word
returns number 1
"""
def test_count_words_one_string():
    result = count_words("one")
    assert result == 1

"""
Given a string of three words
returns number 3
"""
def test_count_words_three_strings():
    result = count_words("one, two, three")
    assert result == 3
"""
Given a string of 12 words
returns number 12
"""
def test_count_words_twelve_strings():
    result = count_words("What a lovely day it is today, I'm so glad it's sunny!")
    assert result == 12