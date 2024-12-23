import pytest
from newrank import convert_to_buddhist_era, convert_grade_to_rank


def test_convert_to_buddhist_era():
    assert convert_to_buddhist_era(20) == 2548  
    assert convert_to_buddhist_era(0) == 2568  
    assert convert_to_buddhist_era(100) == 2468 


def test_convert_grade_to_rank():
    assert convert_grade_to_rank("A") == "High Distinction"
    assert convert_grade_to_rank("B+") == "Distinction"
    assert convert_grade_to_rank("C+") == "Good"
    assert convert_grade_to_rank("F") == "Failed"
    assert convert_grade_to_rank("Z") == "Unknown Rank" 
