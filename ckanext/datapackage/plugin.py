from __future__ import annotations

from ckan import plugins as p

from .actions import datapackage_dataset_show
from .auth import datapackage_auth
from .blueprint import datapackage_blueprint


class DataPackagePlugin(p.SingletonPlugin):
    p.implements(p.IActions, inherit=True)
    p.implements(p.IAuthFunctions, inherit=True)
    p.implements(p.IBlueprint)
    p.implements(p.ITemplateHelpers, inherit=True)

    # IActions

    def get_actions(self):
        return {
            "datapackage_dataset_show": datapackage_dataset_show,
        }

    # IAuthFunctions

    def get_auth_functions(self):
        return {
            "datapackage_dataset_show": datapackage_auth,
        }

    # IBlueprint

    def get_blueprint(self):
        return [datapackage_blueprint]

    # ITemplateHelpers

    #  def get_helpers(self):
    #  return {
    #  "helper_available": utils.helper_available,
    #  "dcat_get_endpoint": utils.get_endpoint,
    #  "dcat_endpoints_enabled": utils.endpoints_enabled,
    #  }
