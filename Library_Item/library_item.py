"""Defines LibraryItem"""

from .genre import Genre
class LibraryItem:

    def __init__(self,
                item_id: int,
                title:str,
                author: str,
                genre: Genre,
                is_borrowed: bool):
        """Initialize LibraryItem and validate its values"""

        if type(item_id) is not int or item_id < 1000:
            raise ValueError("item_id must be a positive value with a minimum of four digits")

        title = title.strip()
        if title == "":
            raise ValueError("Author cannot be an empty string")

        self.__item_id = item_id
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__is_borrowed = is_borrowed

    @property
    def item_id(self) -> int:
        """Returns the item ID"""
        return self.__item_id

    @property
    def title(self) -> str:
        """Returns title"""
        return self.__title

    @property
    def author(self) -> str:
        """Returns author"""
        return self.__author

    @property
    def genre(self) -> Genre:
        """Returns Genre"""
        return self.__genre

    @property
    def is_borrowed(self) -> bool:
        """Returns whether the item is borrowed"""
        return self.__is_borrowed
    
    def __str__(self) -> str:
        """Return the informal string of the item."""

        if self.__is_borrowed:
            availability = "Borrowed"
        else:
            availability = "Available"

        return (
            f"{self.__item_id}: {self.__title} ({self.__author})\n"
            f"STATUS: {availability}"
    )