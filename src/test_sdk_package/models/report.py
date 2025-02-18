"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from test_sdk_package.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class Type(str, Enum):
    LINTING = "linting"
    CHANGES = "changes"


class ReportTypedDict(TypedDict):
    type: NotRequired[Type]


class Report(BaseModel):
    type: Optional[Type] = None
