"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from test_sdk_package.types import BaseModel
from test_sdk_package.utils import FieldMetadata, QueryParamMetadata
from typing_extensions import Annotated, TypedDict


class GetGithubSetupStateRequestTypedDict(TypedDict):
    org: str
    repo: str
    generate_gen_lock_id: str


class GetGithubSetupStateRequest(BaseModel):
    org: Annotated[
        str, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]

    repo: Annotated[
        str, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]

    generate_gen_lock_id: Annotated[
        str, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
