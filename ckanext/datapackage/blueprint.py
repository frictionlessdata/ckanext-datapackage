from __future__ import annotations

from flask import Blueprint, jsonify

datapackage_blueprint = Blueprint(
    "datapackage", __name__, url_defaults={"package_type": "dataset"}
)


@datapackage_blueprint.route("/dataset/<id>/datapackage.json", methods=["GET"])
def read_dataset(id):
    return jsonify({"id": id})
