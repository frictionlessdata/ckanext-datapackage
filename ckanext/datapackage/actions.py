from __future__ import annotations

from ckan.plugins import toolkit
from ckan.types import Context, DataDict


def datapackage_dataset_show(context: Context, data_dict: DataDict):
    toolkit.check_access("datapackage_dataset_show", context, data_dict)
    dataset = toolkit.get_action("package_show")(context, data_dict)
    # TODO: implement mapping
    package = dataset
    return package
