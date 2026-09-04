"""Unit tests for the Genre enumeration"""

from Library_Item.genre import Genre

def test_fiction_value_initialized():
    """Verify fiction is initialized to 100"""
    assert Genre.FICTION.value == 100

def test_non_fiction_value_initialized():
    """Verify non fiction is initialized to 200"""
    assert Genre.NON_FICTION.value == 200

def test_fantasy_value_initialized():
    """Verify fantasy is initialized to 300"""
    assert Genre.FANTASY.value == 300

def test_true_crime_value_initialized():
    """Verify true crime is initialized to 400"""
    assert Genre.TRUE_CRIME.value == 400