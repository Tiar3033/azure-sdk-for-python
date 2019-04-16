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

from .proxy_resource_py3 import ProxyResource


class Connection(ProxyResource):
    """Definition of the connection.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param connection_type: Gets or sets the connectionType of the connection.
    :type connection_type:
     ~azure.mgmt.automation.models.ConnectionTypeAssociationProperty
    :ivar field_definition_values: Gets the field definition values of the
     connection.
    :vartype field_definition_values: dict[str, str]
    :ivar creation_time: Gets the creation time.
    :vartype creation_time: datetime
    :ivar last_modified_time: Gets the last modified time.
    :vartype last_modified_time: datetime
    :param description: Gets or sets the description.
    :type description: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'field_definition_values': {'readonly': True},
        'creation_time': {'readonly': True},
        'last_modified_time': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'connection_type': {'key': 'properties.connectionType', 'type': 'ConnectionTypeAssociationProperty'},
        'field_definition_values': {'key': 'properties.fieldDefinitionValues', 'type': '{str}'},
        'creation_time': {'key': 'properties.creationTime', 'type': 'iso-8601'},
        'last_modified_time': {'key': 'properties.lastModifiedTime', 'type': 'iso-8601'},
        'description': {'key': 'properties.description', 'type': 'str'},
    }

    def __init__(self, *, connection_type=None, description: str=None, **kwargs) -> None:
        super(Connection, self).__init__(**kwargs)
        self.connection_type = connection_type
        self.field_definition_values = None
        self.creation_time = None
        self.last_modified_time = None
        self.description = description
