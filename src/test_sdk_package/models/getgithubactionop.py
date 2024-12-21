"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from test_sdk_package.types import BaseModel
from test_sdk_package.utils import FieldMetadata, QueryParamMetadata
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetGitHubActionRequestTypedDict(TypedDict):
    org: str
    repo: str
    target_name: NotRequired[str]
    r"""The targetName of the workflow target."""


class GetGitHubActionRequest(BaseModel):
    org: Annotated[
        str, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]

    repo: Annotated[
        str, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]

    target_name: Annotated[
        Optional[str],
        pydantic.Field(alias="targetName"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The targetName of the workflow target."""