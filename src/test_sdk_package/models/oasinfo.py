"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from test_sdk_package.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class LicenseTypedDict(TypedDict):
    identifier: NotRequired[str]


class License(BaseModel):
    identifier: Optional[str] = None


class OASInfoTypedDict(TypedDict):
    title: str
    summary: str
    description: str
    version: str
    license: LicenseTypedDict


class OASInfo(BaseModel):
    title: str

    summary: str

    description: str

    version: str

    license: License
