import pytest
from new import calculate_age_and_grade

def test_calculate_age_and_grade():
    result = calculate_age_and_grade("Peter", 1998, 75)
    assert result["name"] == "Peter"
    assert result["age"] == 27
    assert result["grade"] == "B+"

    result = calculate_age_and_grade("Bob", -100, -100)
    assert result["name"] == "Bob"
    assert result["age"] == 2125
    assert result["grade"] == "F"

    result = calculate_age_and_grade("Charlie", 2010, 200)
    assert result["name"] == "Charlie"
    assert result["age"] == 15
    assert result["grade"] == "A"

    result = calculate_age_and_grade("David", 2005, 55)
    assert result["name"] == "David"
    assert result["age"] == 20
    assert result["grade"] == "D+"

    result = calculate_age_and_grade("Eve", 1990, 45)
    assert result["name"] == "Eve"
    assert result["age"] == 35
    assert result["grade"] == "F"
