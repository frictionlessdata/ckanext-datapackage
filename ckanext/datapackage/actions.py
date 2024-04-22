from __future__ import annotations

from ckan.plugins import toolkit
from ckan.types import Context, DataDict
from dplib.plugins.ckan.models import CkanPackage, CkanSchema


def datapackage_dataset_show(context: Context, data_dict: DataDict):
    toolkit.check_access("datapackage_dataset_show", context, data_dict)
    ckan = toolkit.get_action("package_show")(context, data_dict)
    package = CkanPackage.from_dict(ckan).to_dp()
    for resource in package.resources:
        resource_id = resource.custom.get("ckan:id")
        if resource_id:
            try:
                ckan = toolkit.get_action("datastore_info")({}, {"id": resource_id})
                schema = CkanSchema.from_dict(ckan).to_dp()
                resource.schema = schema
                resource.type = "table"
            except Exception:
                pass
    return package.to_dict()
