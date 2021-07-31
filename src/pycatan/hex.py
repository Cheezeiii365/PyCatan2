from typing import Set

from .coords import Coords
from .hex_type import HexType


class Hex:
    """A hex on a Catan board

    Args:
        coords (Coords): The coordinates of this hex
        hex_type (HexType): The type of this hex
        token_number (int, optional): The number of the token on this hex, or None if the hext is a desert

    Attributes:
        CONNECTED_POINTS_OFFSETS (Set[Coords]):
                The offsets of the connected points from a hex's coordinates
        coords (Coords): The coordinates of this hex
        hex_type (HexType): The type of this hex
        token_number (int): The number of the token on this hex
    """

    CONNECTED_CORNER_OFFSETS: Set[Coords] = {
        Coords(1, 0),
        Coords(0, 1),
        Coords(-1, 1),
        Coords(-1, 0),
        Coords(0, -1),
        Coords(1, -1),
    }

    def __init__(self, coords: Coords, hex_type: HexType, token_number: int):
        self.coords = coords
        self.hex_type = hex_type
        self.token_number = token_number
