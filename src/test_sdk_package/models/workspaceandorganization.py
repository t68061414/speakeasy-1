"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .organization import Organization, OrganizationTypedDict
from .workspace import Workspace, WorkspaceTypedDict
from test_sdk_package.types import BaseModel
from typing_extensions import TypedDict


class WorkspaceAndOrganizationTypedDict(TypedDict):
    r"""A workspace and organization"""

    workspace: WorkspaceTypedDict
    r"""A speakeasy workspace"""
    organization: OrganizationTypedDict
    r"""A speakeasy organization"""


class WorkspaceAndOrganization(BaseModel):
    r"""A workspace and organization"""

    workspace: Workspace
    r"""A speakeasy workspace"""

    organization: Organization
    r"""A speakeasy organization"""