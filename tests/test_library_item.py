"""Unit tests for the Library class."""

import pytest

from library_item.genre import Genre
from library_item.library_item import LibraryItem

def make_item(is_borrowed=False):
    return LibraryItem(14924,
                       "Leaves of Grass",
                       "Walt Whitmen",
                       Genre.FICTION,
                       is_borrowed)

def test_init_rejects_item_id_less_than_four():
    """Test that an item ID below four digits raised ValueError"""
    with pytest.raises(ValueError,
                       match=("item_id must be a positive with a minimum of four digits")
                       ):
        LibraryItem(
            999,
            "Title",
            "Author",
            Genre.FICTION,
            False
        )
def test_init_rejects_empty_title():
    """Tests that an empty title raises ValueError"""
    with pytest.raises(
        ValueError,
        match="^title cannot be an empty string$"
    ):
        LibraryItem(
            1000,
            "",
            "Author",
            Genre.FICTION,
            False
        )

def test_init_rejects_empty_author():
    """Test that empty author raises Error"""
    with pytest.raises(
        ValueError,
        match="^author cannot be an empty string$"
    ):
        LibraryItem(
            1000,
            "Title",
            " ",
            Genre.FICTION,
            False
        )

def test_init_creates_new_instance():
    """Tests valid LibraryItem initialized correctly"""
    item = LibraryItem(
        14924,
        " Leaves of Grass ",
        " Walt Whitmen ",
        Genre.FICTION,
        True
    )

    assert isinstance(item, LibraryItem)

    assert item._LibraryItem__item_id == 14924
    assert item._LibraryItem__title == "Leaves of Grass"
    assert item._LibraryItem__author == "Walt Whitmen"
    assert item.__LibraryItem__genre == Genre.FICTION
    assert item._LibraryItem__is_borrowed is True

def test_item_id_property():
    """Test that item_id returns"""
    item = make_item()
    assert item.item_id == item._LibraryItem__item_id

def test_title_property():
    """Tests title returns the current value."""
    item = make_item()
    assert item.title == item._LibraryItem__title

def test_author_property():
    """Test that author returns the current value"""
    item = make_item()
    assert item.author == item._LibraryItem__author

def test_genre_property():
    """Tests genre returns the current value"""
    item = make_item()
    assert item.genre == item._LibraryItem__genre

def test_is_borrowed_property():
    """Tests is_borrowed returns the current value"""
    item = make_item(is_borrowed=True)
    assert item.is_borrowed == item._LibraryItem__is_borrowed



# __str__

def test_str_borrowed_string():
    """Test string representation for borrowed item"""
    item = make_item(is_borrowed=True)
    expected = (
        "14924: Leaves of Grass (Walt Whitmen)\n"
        "STATUS: Borrowed"
    )

    assert str(item) == expected

def test_str_available():
    """Tests string representation for available item"""
    item = make_item(is_borrowed=False)
    expected = (
        "14924: Leaves of Grass (Walt Whitmen)\n"
        "STATUS: Available"
    )

    assert str(item) == expected