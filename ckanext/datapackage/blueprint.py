from __future__ import annotations

from ckan.plugins import toolkit
from flask import Blueprint, jsonify

datapackage_blueprint = Blueprint(
    "datapackage", __name__, url_defaults={"package_type": "dataset"}
)


@datapackage_blueprint.route("/dataset/<id>/datapackage.json", methods=["GET"])
def read_dataset(id, package_type=None):
    try:
        data = toolkit.get_action("datapackage_dataset_show")({}, {"id": id})
        return jsonify(data)
    except toolkit.ObjectNotFound:
        toolkit.abort(404)
    except Exception:
        toolkit.abort(500)
