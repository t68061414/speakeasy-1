"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from test_sdk_package.types import BaseModel
from typing_extensions import TypedDict


class RemoteDocumentTypedDict(TypedDict):
    r"""A document hosted in the registry"""

    registry_url: str


class RemoteDocument(BaseModel):
    r"""A document hosted in the registry"""

    registry_url: str
