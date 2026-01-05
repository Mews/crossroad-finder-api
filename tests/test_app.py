from flask.testing import FlaskClient


def test_app_get_root(client: FlaskClient):
    response = client.get("/")
    assert response.status_code == 302


def test_invalid_data_missing_game_version(client: FlaskClient, payload):
    payload.pop("game_version")

    response = client.post("/", json=payload)

    assert response.status_code == 400


def test_invalid_data_missing_world_seed(client: FlaskClient, payload):
    payload.pop("world_seed")

    response = client.post("/", json=payload)

    assert response.status_code == 400


def test_invalid_data_missing_fortress_salt(client: FlaskClient, payload):
    payload.pop("fortress_salt")

    response = client.post("/", json=payload)

    assert response.status_code == 400


def test_invalid_data_missing_crossroad_shape(client: FlaskClient, payload):
    payload.pop("crossroad_shape")

    response = client.post("/", json=payload)

    assert response.status_code == 400


def test_invalid_data_missing_max_y(client: FlaskClient, payload):
    payload.pop("max_y")

    response = client.post("/", json=payload)

    assert response.status_code == 400


def test_invalid_data_missing_search_radius(client: FlaskClient, payload):
    payload.pop("search_radius")

    response = client.post("/", json=payload)

    assert response.status_code == 400


def test_invalid_data_missing_search_center_x(client: FlaskClient, payload):
    payload.pop("search_center_x")

    response = client.post("/", json=payload)

    assert response.status_code == 400


def test_invalid_data_missing_search_center_z(client: FlaskClient, payload):
    payload.pop("search_center_z")

    response = client.post("/", json=payload)

    assert response.status_code == 400


def test_invalid_data_version_too_old(client: FlaskClient, payload):
    payload["game_version"] = "1.6.4"

    response = client.post("/", json=payload)

    assert response.status_code == 400


def test_invalid_data_version_wrong_format(client: FlaskClient, payload):
    payload["game_version"] = "26w48a"

    response = client.post("/", json=payload)

    assert response.status_code == 400


def test_invalid_data_version_wrong_type(client: FlaskClient, payload):
    payload["game_version"] = 123

    response = client.post("/", json=payload)

    assert response.status_code == 400


def test_invalid_data_world_seed_wrong_type(client: FlaskClient, payload):
    payload["world_seed"] = "hello"

    response = client.post("/", json=payload)

    assert response.status_code == 400


def test_invalid_data_fortress_salt_wrong_type(client: FlaskClient, payload):
    payload["fortress_salt"] = "hello"

    response = client.post("/", json=payload)

    assert response.status_code == 400


def test_invalid_data_invalid_crossroad_shape(client: FlaskClient, payload):
    payload["crossroad_shape"] = "NOT_A_SHAPE"

    response = client.post("/", json=payload)

    assert response.status_code == 400


def test_invalid_data_crossroad_shape_invalid_type(client: FlaskClient, payload):
    payload["crossroad_shape"] = 0

    response = client.post("/", json=payload)

    assert response.status_code == 400


def test_invalid_data_max_y_invalid_type(client: FlaskClient, payload):
    payload["max_y"] = "hello"

    response = client.post("/", json=payload)

    assert response.status_code == 400


def test_invalid_data_max_y_too_low(client: FlaskClient, payload):
    payload["max_y"] = 0

    response = client.post("/", json=payload)

    assert response.status_code == 400


def test_invalid_data_max_y_too_high(client: FlaskClient, payload):
    payload["max_y"] = 256

    response = client.post("/", json=payload)

    assert response.status_code == 400


def test_invalid_data_search_radius_invalid_type(client: FlaskClient, payload):
    payload["search_radius"] = "hello"

    response = client.post("/", json=payload)

    assert response.status_code == 400


def test_invalid_data_search_radius_too_large(client: FlaskClient, payload):
    payload["search_radius"] = 60_000_001

    response = client.post("/", json=payload)

    assert response.status_code == 400


def test_invalid_data_search_center_x_invalid_type(client: FlaskClient, payload):
    payload["search_center_x"] = "hello"

    response = client.post("/", json=payload)

    assert response.status_code == 400


def test_invalid_data_search_center_x_too_low(client: FlaskClient, payload):
    payload["search_center_x"] = -30_000_001

    response = client.post("/", json=payload)

    assert response.status_code == 400


def test_invalid_data_search_center_x_too_high(client: FlaskClient, payload):
    payload["search_center_x"] = 30_000_001

    response = client.post("/", json=payload)

    assert response.status_code == 400


def test_invalid_data_search_center_z_invalid_type(client: FlaskClient, payload):
    payload["search_center_z"] = "hello"

    response = client.post("/", json=payload)

    assert response.status_code == 400


def test_invalid_data_search_center_z_too_low(client: FlaskClient, payload):
    payload["search_center_z"] = -30_000_001

    response = client.post("/", json=payload)

    assert response.status_code == 400


def test_invalid_data_search_center_z_too_high(client: FlaskClient, payload):
    payload["search_center_z"] = 30_000_001

    response = client.post("/", json=payload)

    assert response.status_code == 400


def test_valid_data(client: FlaskClient, payload):
    response = client.post("/", json=payload)

    assert response.status_code == 200

    crossroads = response.json["crossroads"]

    assert len(crossroads) == 2

    assert [-1118, 54, -2062] in crossroads
    assert [2418, 50, 1257] in crossroads


def test_valid_data_non_stripped_strings(client: FlaskClient, payload):
    payload["game_version"] = "  1.21.11  "
    payload["crossroad_shape"] = "  QUAD_LINE  "

    response = client.post("/", json=payload)

    assert response.status_code == 200

    crossroads = response.json["crossroads"]

    assert len(crossroads) == 2

    assert [-1118, 54, -2062] in crossroads
    assert [2418, 50, 1257] in crossroads


def test_valid_data_all_data_as_strings(client: FlaskClient, payload):
    payload["fortress_salt"] = 30084232

    for key, value in payload.items():
        payload[key] = str(value)

    response = client.post("/", json=payload)

    assert response.status_code == 200

    crossroads = response.json["crossroads"]

    assert len(crossroads) == 2

    assert [-1118, 54, -2062] in crossroads
    assert [2418, 50, 1257] in crossroads
