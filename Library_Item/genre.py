"""Defines the genre are available for library items"""

from enum import Enum

class Genre(Enum):
    """Enum representing the category of an artistic composition."""

    FICTION = 100
    NON_FICTION = 200
    FANTASY = 300
    TRUE_CRIME = 400
    