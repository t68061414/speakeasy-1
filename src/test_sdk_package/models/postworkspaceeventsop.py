"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .clievent import CliEvent, CliEventTypedDict
from test_sdk_package.types import BaseModel
from test_sdk_package.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PostWorkspaceEventsGlobalsTypedDict(TypedDict):
    workspace_id: NotRequired[str]


class PostWorkspaceEventsGlobals(BaseModel):
    workspace_id: Annotated[
        Optional[str],
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ] = None


class PostWorkspaceEventsRequestTypedDict(TypedDict):
    request_body: List[CliEventTypedDict]
    workspace_id: NotRequired[str]
    r"""Unique identifier of the workspace."""


class PostWorkspaceEventsRequest(BaseModel):
    request_body: Annotated[
        List[CliEvent],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    workspace_id: Annotated[
        Optional[str],
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ] = None
    r"""Unique identifier of the workspace."""