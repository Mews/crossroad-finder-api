[![Tests](https://github.com/Mews/crossroad-finder-api/actions/workflows/tests.yaml/badge.svg)](https://github.com/Mews/crossroad-finder-api/actions/workflows/tests.yaml) [![Coverage badge](https://github.com/Mews/crossroad-finder-api/raw/python-coverage-comment-action-data/badge.svg)](https://github.com/Mews/crossroad-finder-api/tree/python-coverage-comment-action-data)

# crossroad-finder-api

A flask api that uses the [CrossroadFinder tool](https://github.com/Gaider10/CrossroadFinder) by [Gaider10](https://github.com/Gaider10) to find nether fortress patterns.

## Usage

To use the api send a `POST` request to the root endpoint with the following json data:

| key             | type                | description                                                                                                                           | restrictions                                                                                                                                                                                                                                      |
|-----------------|---------------------|---------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| game_version    | `string`            | Minecraft version to search on                                                                                                        | A string in the standard format `Major.Minor.Patch` used by Mojang (Ex.: "1.21.11" or "1.16" ("1.16.0" would also work)<br>Snapshots aren't currently supported, but in most cases you can just use the latest full release prior to the snapshot |
| world_seed      | `integer`           | Seed of the Minecraft world to search on                                                                                              | None, other than type                                                                                                                                                                                                                             |
| fortress_salt   | `integer` OR `null` | Fortress salt value (only for 1.16.1+). Should generally be set to `null` to use the default value, unless you know what you're doing | None, other than type                                                                                                                                                                                                                             |
| crossroad_shape | `string`            | Crossroad shape to find                                                                                                               | One of `DOUBLE`, `TRIPLE_LINE`, `QUAD_LINE`, `QUINT_LINE`, `TRIPLE_CORNER`, `QUAD_SQUARE`, `QUINT_BLOB`                                                                                                                                           |
| max_y           | `integer`           | Highest Y layer that the crossroads can be at                                                                                         | Inside range [1, 255]                                                                                                                                                                                                                             |
| search_radius   | `integer`           | Radius around the search center to search for                                                                                         | Inside range [0, 60 000 000]                                                                                                                                                                                                                      |
| search_center_x | `integer`           | X component of the search center position                                                                                             | Inside range [-30 000 000, 30 000 000]                                                                                                                                                                                                            |
| search_center_z | `integer`           | Z component of the search center position                                                                                             | Inside range [-30 000 000, 30 000 000]                                                                                                                                                                                                            |

Example data:
```json
{
    "game_version": "1.21.11",
    "world_seed": 448000115,
    "fortress_salt":  null,
    "crossroad_shape": "QUAD_LINE",
    "max_y": 255,
    "search_radius": 10000,
    "search_center_x": 0,
    "search_center_z": 0
}
```

The returned JSON data will look like this:
```json
{
    "crossroads": [
        [-10391, 62, -5886],
        [-10094, 69, -2432],
        [-3671, 59, 671],
        [281, 48, -8878],
        [569, 52, -334],
        [4386, 52, 2770],
        [6642, 69, -9703],
        [6504, 69, -5822],
        [7529, 52, 10658],
        [8018, 59, -3646]
    ]
}
```

As of right now the api is hosted at `https://mews.pythonanywhere.com/`

