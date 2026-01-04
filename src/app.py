from flask import Flask, redirect, request, jsonify
from marshmallow import ValidationError

from internal.schema import InputSchema
from internal import finder

app = Flask(__name__)

@app.route("/", methods=["GET"])
def root():
    return redirect("https://github.com/Mews/crossroad-finder-api")


@app.route("/", methods=["POST"])
def find_crossroads():
    json_data = request.get_json()

    schema = InputSchema()

    try:
        json_data = schema.load(json_data)
    except ValidationError as error:
        return jsonify(
            {"error": "Invalid JSON", "details": error.messages}
        ), 400

    options = finder.FinderOptions(
        game_version=json_data["game_version"],
        world_seed=json_data["world_seed"],
        fortress_salt=json_data["fortress_salt"],
        crossroad_shape=json_data["crossroad_shape"],
        max_y=json_data["max_y"],
        search_radius=json_data["search_radius"],
        search_center_x=json_data["search_center_x"],
        search_center_z=json_data["search_center_z"]
    )

    crossroads = finder.find_crossroads(options)

    return jsonify(
        {"crossroads": crossroads}
    ), 200
    

if __name__ == "__main__":
    app.run()
