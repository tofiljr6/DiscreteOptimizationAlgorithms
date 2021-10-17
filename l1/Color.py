from enum import Enum


class Color(Enum):
    """Enum class for Node - visited or no"""
    WHITE = 0
    GRAY = 1
    BLACK = 2