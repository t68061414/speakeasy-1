"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from test_sdk_package.types import BaseModel
from test_sdk_package.utils import FieldMetadata, PathParamMetadata
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class DeleteWorkspaceTokenGlobalsTypedDict(TypedDict):
    workspace_id: NotRequired[str]


class DeleteWorkspaceTokenGlobals(BaseModel):
    workspace_id: Annotated[
        Optional[str],
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ] = None


class DeleteWorkspaceTokenRequestTypedDict(TypedDict):
    token_id: str
    r"""Unique identifier of the token."""
    workspace_id: NotRequired[str]
    r"""Unique identifier of the workspace."""


class DeleteWorkspaceTokenRequest(BaseModel):
    token_id: Annotated[
        str,
        pydantic.Field(alias="tokenID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier of the token."""

    workspace_id: Annotated[
        Optional[str],
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ] = None
    r"""Unique identifier of the workspace."""