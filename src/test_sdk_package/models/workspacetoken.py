"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from pydantic import model_serializer
from test_sdk_package.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from typing_extensions import NotRequired, TypedDict


class WorkspaceTokenTypedDict(TypedDict):
    r"""A workspace token"""

    id: str
    name: str
    workspace_id: str
    alg: str
    key: str
    created_at: datetime
    last_used: NotRequired[Nullable[datetime]]
    created_by: NotRequired[Nullable[str]]
    email: NotRequired[Nullable[str]]


class WorkspaceToken(BaseModel):
    r"""A workspace token"""

    id: str

    name: str

    workspace_id: str

    alg: str

    key: str

    created_at: datetime

    last_used: OptionalNullable[datetime] = UNSET

    created_by: OptionalNullable[str] = UNSET

    email: OptionalNullable[str] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["last_used", "created_by", "email"]
        nullable_fields = ["last_used", "created_by", "email"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
