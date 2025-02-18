"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from test_sdk_package.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class GithubPublishingPRResponseTypedDict(TypedDict):
    r"""Open generation PRs pending publishing"""

    generation_pull_request: NotRequired[str]
    pending_version: NotRequired[str]


class GithubPublishingPRResponse(BaseModel):
    r"""Open generation PRs pending publishing"""

    generation_pull_request: Optional[str] = None

    pending_version: Optional[str] = None
