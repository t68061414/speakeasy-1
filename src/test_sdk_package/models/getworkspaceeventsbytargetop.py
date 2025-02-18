"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from test_sdk_package.types import BaseModel
from test_sdk_package.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetWorkspaceEventsByTargetGlobalsTypedDict(TypedDict):
    workspace_id: NotRequired[str]


class GetWorkspaceEventsByTargetGlobals(BaseModel):
    workspace_id: Annotated[
        Optional[str],
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ] = None


class GetWorkspaceEventsByTargetRequestTypedDict(TypedDict):
    target_id: str
    r"""Filter to only return events corresponding to a particular gen_lock_id (gen_lock_id uniquely identifies a target)"""
    workspace_id: NotRequired[str]
    r"""Unique identifier of the workspace."""
    after_created_at: NotRequired[datetime]
    r"""Filter to only return events created after this timestamp"""


class GetWorkspaceEventsByTargetRequest(BaseModel):
    target_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Filter to only return events corresponding to a particular gen_lock_id (gen_lock_id uniquely identifies a target)"""

    workspace_id: Annotated[
        Optional[str],
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ] = None
    r"""Unique identifier of the workspace."""

    after_created_at: Annotated[
        Optional[datetime],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter to only return events created after this timestamp"""
