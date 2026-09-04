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
