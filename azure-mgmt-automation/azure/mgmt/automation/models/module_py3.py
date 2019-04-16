# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .tracked_resource_py3 import TrackedResource


class Module(TrackedResource):
    """Definition of the module type.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: The Azure Region where the resource lives
    :type location: str
    :param is_global: Gets or sets the isGlobal flag of the module.
    :type is_global: bool
    :param version: Gets or sets the version of the module.
    :type version: str
    :param size_in_bytes: Gets or sets the size in bytes of the module.
    :type size_in_bytes: long
    :param activity_count: Gets or sets the activity count of the module.
    :type activity_count: int
    :param provisioning_state: Gets or sets the provisioning state of the
     module. Possible values include: 'Created', 'Creating',
     'StartingImportModuleRunbook', 'RunningImportModuleRunbook',
     'ContentRetrieved', 'ContentDownloaded', 'ContentValidated',
     'ConnectionTypeImported', 'ContentStored', 'ModuleDataStored',
     'ActivitiesStored', 'ModuleImportRunbookComplete', 'Succeeded', 'Failed',
     'Cancelled', 'Updating'
    :type provisioning_state: str or
     ~azure.mgmt.automation.models.ModuleProvisioningState
    :param content_link: Gets or sets the contentLink of the module.
    :type content_link: ~azure.mgmt.automation.models.ContentLink
    :param error: Gets or sets the error info of the module.
    :type error: ~azure.mgmt.automation.models.ModuleErrorInfo
    :param creation_time: Gets or sets the creation time.
    :type creation_time: datetime
    :param last_modified_time: Gets or sets the last modified time.
    :type last_modified_time: datetime
    :param description: Gets or sets the description.
    :type description: str
    :param is_composite: Gets or sets type of module, if its composite or not.
    :type is_composite: bool
    :param etag: Gets or sets the etag of the resource.
    :type etag: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'is_global': {'key': 'properties.isGlobal', 'type': 'bool'},
        'version': {'key': 'properties.version', 'type': 'str'},
        'size_in_bytes': {'key': 'properties.sizeInBytes', 'type': 'long'},
        'activity_count': {'key': 'properties.activityCount', 'type': 'int'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'ModuleProvisioningState'},
        'content_link': {'key': 'properties.contentLink', 'type': 'ContentLink'},
        'error': {'key': 'properties.error', 'type': 'ModuleErrorInfo'},
        'creation_time': {'key': 'properties.creationTime', 'type': 'iso-8601'},
        'last_modified_time': {'key': 'properties.lastModifiedTime', 'type': 'iso-8601'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'is_composite': {'key': 'properties.isComposite', 'type': 'bool'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, *, tags=None, location: str=None, is_global: bool=None, version: str=None, size_in_bytes: int=None, activity_count: int=None, provisioning_state=None, content_link=None, error=None, creation_time=None, last_modified_time=None, description: str=None, is_composite: bool=None, etag: str=None, **kwargs) -> None:
        super(Module, self).__init__(tags=tags, location=location, **kwargs)
        self.is_global = is_global
        self.version = version
        self.size_in_bytes = size_in_bytes
        self.activity_count = activity_count
        self.provisioning_state = provisioning_state
        self.content_link = content_link
        self.error = error
        self.creation_time = creation_time
        self.last_modified_time = last_modified_time
        self.description = description
        self.is_composite = is_composite
        self.etag = etag
