"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from test_sdk_package.types import BaseModel
from test_sdk_package.utils import FieldMetadata, QueryParamMetadata
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class LinkGithubAccessRequestTypedDict(TypedDict):
    installation_id: NotRequired[str]
    github_org: NotRequired[str]
    github_oidc_token: NotRequired[str]


class LinkGithubAccessRequest(BaseModel):
    installation_id: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    github_org: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    github_oidc_token: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
