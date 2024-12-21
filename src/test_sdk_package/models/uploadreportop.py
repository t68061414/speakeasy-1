"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .report import Report, ReportTypedDict
import io
import pydantic
from test_sdk_package.types import BaseModel
from test_sdk_package.utils import FieldMetadata, MultipartFormMetadata
from typing import IO, Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


class FileTypedDict(TypedDict):
    file_name: str
    content: Union[bytes, IO[bytes], io.BufferedReader]
    content_type: NotRequired[str]


class File(BaseModel):
    file_name: Annotated[
        str, pydantic.Field(alias="fileName"), FieldMetadata(multipart=True)
    ]

    content: Annotated[
        Union[bytes, IO[bytes], io.BufferedReader],
        pydantic.Field(alias=""),
        FieldMetadata(multipart=MultipartFormMetadata(content=True)),
    ]

    content_type: Annotated[
        Optional[str],
        pydantic.Field(alias="Content-Type"),
        FieldMetadata(multipart=True),
    ] = None


class UploadReportRequestBodyTypedDict(TypedDict):
    r"""The report file to upload provided as a multipart/form-data file segment."""

    data: ReportTypedDict
    file: FileTypedDict


class UploadReportRequestBody(BaseModel):
    r"""The report file to upload provided as a multipart/form-data file segment."""

    data: Annotated[Report, FieldMetadata(multipart=MultipartFormMetadata(json=True))]

    file: Annotated[File, FieldMetadata(multipart=MultipartFormMetadata(file=True))]


class UploadReportUploadedReportTypedDict(TypedDict):
    r"""OK"""

    url: str


class UploadReportUploadedReport(BaseModel):
    r"""OK"""

    url: str
