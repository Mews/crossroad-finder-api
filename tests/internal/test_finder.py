from src.internal import finder


def test_generate_cin_input_post_1_16_1():
    options = finder.FinderOptions(
        game_version="1.16.1",
        world_seed=12345,
        fortress_salt=None,
        crossroad_shape="DOUBLE",
        max_y=255,
        search_radius=1_000,
        search_center_x=0,
        search_center_z=0,
    )

    cin_input = finder.generate_cin_input(options)

    assert cin_input == "2\n12345\n\n0\n255\n1000\n0\n0\n"


def test_generate_cin_input_pre_1_16_1():
    options = finder.FinderOptions(
        game_version="1.16",
        world_seed=12345,
        fortress_salt=None,
        crossroad_shape="DOUBLE",
        max_y=255,
        search_radius=1_000,
        search_center_x=0,
        search_center_z=0,
    )

    cin_input = finder.generate_cin_input(options)

    assert cin_input == "1\n12345\n0\n255\n1000\n0\n0\n"


def test_finder():
    options = finder.FinderOptions(
        game_version="1.21.11",
        world_seed=12345,
        fortress_salt=None,
        crossroad_shape="QUAD_LINE",
        max_y=255,
        search_radius=2000,
        search_center_x=0,
        search_center_z=0,
    )

    crossroads = finder.find_crossroads(options)

    assert len(crossroads) == 2

    assert (-1118, 54, -2062) in crossroads
    assert (2418, 50, 1257) in crossroads
