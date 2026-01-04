import sys, os

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))
sys.path.insert(0, src_path)

# From https://flask.palletsprojects.com/en/stable/testing/

import pytest
from src.app import app as flask_app

@pytest.fixture()
def app():
    flask_app.config.update({
        "TESTING": True,
    })

    yield flask_app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def payload():
    return {
        "game_version": "1.21.11",
        "world_seed": 12345,
        "fortress_salt": None,
        "crossroad_shape": "QUAD_LINE",
        "max_y": 255,
        "search_radius": 2000,
        "search_center_x": 0,
        "search_center_z": 0
    }
