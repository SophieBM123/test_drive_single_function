from lib.make_snippet import *

"""
Given an empty string
It returns an empty string 
"""

def test_make_snippet_returns_empty_string():
    result = make_snippet(" ")
    assert result == " "

"""
Given a string of four words
It returns four words words.
"""

def test_make_snippet_first_four_words():
    result = make_snippet("Hello what a day!")
    assert result == "Hello what a day!"

""""
Given a string of four words
It returns all four words
"""

def test_make_snipped_first_five_words():
    result = make_snippet("Hello what a day!")
    assert result == "Hello what a day!"

""""
Given a string of five words
It returns first five words
"""

def test_make_snipped_first_five_words():
    result = make_snippet("Hello what a nice day")
    assert result == "Hello what a nice day"

""""
Given a string of more than 5 words
It returns first five words followed by ellipses 
"""

def test_make_snipped_first_five_words_and_if_more_add_ellipses():
    result = make_snippet("Hello what a nice day it is today!")
    assert result == "Hello what a nice day..."
