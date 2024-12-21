"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from test_sdk_package.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class GithubMissingPublishingSecretsResponseTypedDict(TypedDict):
    r"""A valid response containing MISSING publishing secret keys for a github target"""

    missing_secrets: NotRequired[List[str]]


class GithubMissingPublishingSecretsResponse(BaseModel):
    r"""A valid response containing MISSING publishing secret keys for a github target"""

    missing_secrets: Optional[List[str]] = None
