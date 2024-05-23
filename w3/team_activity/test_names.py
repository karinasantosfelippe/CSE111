"""
Author: Karina Santos Felippe
Problem Statement:
    Most people around the world today have at least two names, a family name and a given name. In the United States, we usually write a person’s given name followed by his family name. However, when a computer lists names in alphabetical order, it is convenient to list the family name first and then the given name like this:

        Toussaint; Marie
        Toussaint; Olivier
        Washington; George
        Washington; Martha

    When writing a program that alphabetizes names, it is often helpful to have the following three functions.

    make_full_name
        Combines a person’s given name and family name into one string with the family name first
    extract_family_name
        Extracts a person’s family name from his full name
    extract_given_name
        Extracts a person’s given name from his full name
        
    A programmer has already written those three functions. However, there are mistakes in at least two of the three functions.
"""

from CSE111.w3.team_activity.names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("", "") == "; "
    assert make_full_name("a", "Tr") == "Tr; a"
    assert make_full_name("Name", "Hyphenated-Name") == "Hyphenated-Name; Name"
    assert make_full_name("Karina", "Felippe") == "Felippe; Karina"

def test_extract_family_name():
    assert extract_family_name("; ") == ""
    assert extract_family_name("Tr; a") == "Tr"
    assert extract_family_name("Hyphenated-Name; Name") == "Hyphenated-Name"
    assert extract_family_name("Felippe; Karina") == "Felippe"

def test_extract_given_name():
    assert extract_given_name("; ") == ""
    assert extract_given_name("Tr; a") == "a"
    assert extract_given_name("Hyphenated-Name; Name") == "Name"
    assert extract_given_name("Felippe; Karina") == "Karina"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])