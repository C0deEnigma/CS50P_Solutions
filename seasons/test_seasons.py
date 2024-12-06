from seasons import valid_dob
from seasons import convert_to_words
def test_valid_dob():
    assert valid_dob('January 1,1999') == False
    assert valid_dob('21-09-2006')==False
    assert valid_dob('2006-12-12')==True
def test_convert_to_words():
    assert convert_to_words(525600)=='Five hundred twenty-five thousand, six hundred minutes'
    assert convert_to_words(2629440)=='Two million, six hundred twenty-nine thousand, four hundred forty minutes'
    assert convert_to_words(15632)=='Fifteen thousand, six hundred thirty-two minutes'
    assert convert_to_words(5632)=='Five thousand, six hundred thirty-two minutes'
    assert convert_to_words(611)=='Six hundred eleven minutes'
