from marshmallow import (Schema, ValidationError, fields, pre_load, validate,
                         validates)

from internal.parser import MinecraftVersion, get_minecraft_version_from_str


class InputSchema(Schema):
    @pre_load
    def strip_strings(self, data, **kwargs):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = value.strip()

        return data

    @validates("game_version")
    def validate_min_version(self, value, **kwargs):
        version = get_minecraft_version_from_str(value)

        if version < MinecraftVersion(1, 7, 0):
            raise ValidationError("Minecraft version must be 1.7.0 or newer")

    game_version = fields.String(
        required=True, validate=validate.Regexp(r"^\d+\.\d+(?:\.\d+)?$")
    )

    world_seed = fields.Integer(required=True)

    fortress_salt = fields.Integer(required=True, allow_none=True)

    crossroad_shape = fields.String(
        required=True,
        validate=validate.OneOf(
            [
                "DOUBLE",
                "TRIPLE_LINE",
                "QUAD_LINE",
                "QUINT_LINE",
                "TRIPLE_CORNER",
                "QUAD_SQUARE",
                "QUINT_BLOB",
            ]
        ),
    )

    max_y = fields.Integer(required=True, validate=validate.Range(min=1, max=255))

    search_radius = fields.Integer(
        required=True, validate=validate.Range(min=0, max=60_000_000)
    )

    search_center_x = fields.Integer(
        required=True, validate=validate.Range(min=-30_000_000, max=30_000_000)
    )
    search_center_z = fields.Integer(
        required=True, validate=validate.Range(min=-30_000_000, max=30_000_000)
    )
