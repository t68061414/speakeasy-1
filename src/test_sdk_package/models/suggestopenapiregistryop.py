"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .suggestrequestbody import SuggestRequestBody, SuggestRequestBodyTypedDict
import pydantic
from test_sdk_package.types import BaseModel
from test_sdk_package.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    RequestMetadata,
)
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class SuggestOpenAPIRegistryRequestTypedDict(TypedDict):
    x_session_id: str
    namespace_name: str
    revision_reference: str
    r"""Tag or digest"""
    suggest_request_body: NotRequired[SuggestRequestBodyTypedDict]
    r"""Suggest options"""


class SuggestOpenAPIRegistryRequest(BaseModel):
    x_session_id: Annotated[
        str,
        pydantic.Field(alias="x-session-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ]

    namespace_name: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    revision_reference: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Tag or digest"""

    suggest_request_body: Annotated[
        Optional[SuggestRequestBody],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None
    r"""Suggest options"""
