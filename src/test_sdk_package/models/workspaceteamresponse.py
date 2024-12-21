"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .ssometadata import SSOMetadata, SSOMetadataTypedDict
from .user import User, UserTypedDict
from test_sdk_package.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class WorkspaceTeamResponseTypedDict(TypedDict):
    r"""Workspace team response"""

    users: List[UserTypedDict]
    sso_metadata: NotRequired[SSOMetadataTypedDict]
    r"""SSO metadata for a workspace"""


class WorkspaceTeamResponse(BaseModel):
    r"""Workspace team response"""

    users: List[User]

    sso_metadata: Optional[SSOMetadata] = None
    r"""SSO metadata for a workspace"""
