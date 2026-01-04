import pytest

from src.internal import parser


@pytest.mark.parametrize(
    "version_string,expected",
    [
        ("1.7", 0),
        ("1.7.0", 0),
        ("1.7.10", 0),
        ("1.12.2", 0),
        ("1.13", 1),
        ("1.13.0", 1),
        ("1.15.2", 1),
        ("1.16", 1),
        ("1.16.1", 2),
        ("1.16.5", 2),
        ("1.17.1", 2),
        ("1.18", 3),
        ("1.19.4", 3),
        ("1.20.0", 3),
        ("1.21.5", 3),
        ("1.21.11", 3),
        ("1.30.5", 3),
    ],
)
def test_parse_game_version_input(version_string, expected):
    assert parser.parse_game_version_input(version_string) == str(expected)


def test_parse_fortress_salt():
    assert parser.parse_fortress_salt(None) == ""
    assert parser.parse_fortress_salt(12345) == "12345"
