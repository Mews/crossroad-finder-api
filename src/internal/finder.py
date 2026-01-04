import platform
import subprocess
from dataclasses import dataclass
from typing import Optional

from internal import parser
from internal.parser import CrossroadShape, MinecraftVersion


@dataclass(order=True)
class FinderOptions:
    game_version: str
    world_seed: int
    fortress_salt: Optional[int]
    crossroad_shape: str
    max_y: int
    search_radius: int
    search_center_x: int
    search_center_z: int


def generate_cin_input(options: FinderOptions):
    cin_input = ""

    cin_input += parser.parse_game_version_input(options.game_version) + "\n"

    cin_input += str(options.world_seed) + "\n"

    if parser.get_minecraft_version_from_str(options.game_version) >= MinecraftVersion(
        1, 16, 1
    ):
        cin_input += parser.parse_fortress_salt(options.fortress_salt) + "\n"

    cin_input += str(CrossroadShape[options.crossroad_shape].value) + "\n"

    cin_input += str(options.max_y) + "\n"

    cin_input += str(options.search_radius) + "\n"

    cin_input += str(options.search_center_x) + "\n"

    cin_input += str(options.search_center_z) + "\n"

    return cin_input


def find_crossroads(options: FinderOptions):
    if platform.system() == "Windows":
        bin_path = "bin/crossroadfinder_win.exe"
    else:
        bin_path = "bin/crossroadfinder_linux.exe"

    result = subprocess.run(
        bin_path, input=generate_cin_input(options), text=True, capture_output=True
    )

    crossroads = []

    for line in result.stdout.split("\n"):
        if "Found a good shape at /tp " in line:
            coords_str = line.removeprefix("Found a good shape at /tp ").strip()
            coords = tuple(int(coord) for coord in coords_str.split(" "))
            crossroads.append(coords)

    return crossroads
