from __future__ import annotations

from ckan.plugins import toolkit
from ckan.types import Context, DataDict


@toolkit.auth_allow_anonymous_access
def datapackage_auth(context: Context, data_dict: DataDict):
    """
    All users can access DCAT endpoints by default
    """
    return {"success": True}
