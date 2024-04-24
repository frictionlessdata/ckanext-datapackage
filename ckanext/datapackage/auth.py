from __future__ import annotations

from ckan.plugins import toolkit
from ckan.types import Context, DataDict

# See in ckanext-dcat:
# https://github.com/ckan/ckanext-dcat/blob/master/ckanext/dcat/logic.py#L211


@toolkit.auth_allow_anonymous_access
def datapackage_auth(context: Context, data_dict: DataDict):
    """
    All users can access Data Package endpoint by default
    """
    return {"success": True}
