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


class FeatureFlagTypedDict(TypedDict):
    r"""A feature flag is a key-value pair that can be used to enable or disable features."""

    feature_flag: str
    trial_ends_at: NotRequired[Nullable[datetime]]


class FeatureFlag(BaseModel):
    r"""A feature flag is a key-value pair that can be used to enable or disable features."""

    feature_flag: str

    trial_ends_at: OptionalNullable[datetime] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["trial_ends_at"]
        nullable_fields = ["trial_ends_at"]
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
