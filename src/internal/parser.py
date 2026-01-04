from dataclasses import dataclass
from enum import Enum

@dataclass(order=True)
class MinecraftVersion:
    major: int
    minor: int
    patch: int


class CrossroadShape(Enum):
    DOUBLE = 0
    TRIPLE_LINE = 1
    QUAD_LINE = 2
    QUINT_LINE = 3
    TRIPLE_CORNER = 4
    QUAD_SQUARE = 5
    QUINT_BLOB = 6


def get_minecraft_version_from_str(version_string:str) -> MinecraftVersion:
    major = int(version_string.split(".")[0])
    minor = int(version_string.split(".")[1])

    if (len(version_string.split(".")) == 3): patch = int(version_string.split(".")[2])
    else: patch = 0

    return MinecraftVersion(major, minor, patch)


def parse_game_version_input(version_string:str) -> str:
    options = {
        0: MinecraftVersion(1, 7, 0),
        1: MinecraftVersion(1, 13, 0),
        2: MinecraftVersion(1, 16, 1),
        3: MinecraftVersion(1, 18, 0)
    }

    version = get_minecraft_version_from_str(version_string)

    option = 0

    for (key, value) in options.items():
        if value <= version:
            option = key
    
    return str(option)


def parse_fortress_salt(salt_value:int) -> str:
    if salt_value is None:
        return ""
    
    return str(salt_value)
