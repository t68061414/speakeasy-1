"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .httpclient import AsyncHttpClient, HttpClient
from .sdkconfiguration import SDKConfiguration
from .utils.logger import Logger, get_default_logger
from .utils.retries import RetryConfig
from enum import Enum
import httpx
from test_sdk_package import models, utils
from test_sdk_package._hooks import HookContext, SDKHooks
from test_sdk_package.artifacts import Artifacts
from test_sdk_package.auth import Auth
from test_sdk_package.events import Events
from test_sdk_package.github import Github
from test_sdk_package.models import internal
from test_sdk_package.organizations import Organizations
from test_sdk_package.reports import Reports
from test_sdk_package.shorturls import ShortURLs
from test_sdk_package.subscriptions import Subscriptions
from test_sdk_package.suggest import Suggest
from test_sdk_package.types import OptionalNullable, UNSET
from test_sdk_package.utils import get_security_from_env
from test_sdk_package.workspaces import Workspaces
from typing import Any, Callable, Dict, List, Mapping, Optional, Union


class GenerateCodeSamplePreviewAcceptEnum(str, Enum):
    APPLICATION_JSON = "application/json"
    APPLICATION_X_YAML = "application/x-yaml"


class GetCodeSamplePreviewAsyncAcceptEnum(str, Enum):
    APPLICATION_JSON = "application/json"
    APPLICATION_X_YAML = "application/x-yaml"


class TestSdk2(BaseSDK):
    r"""Speakeasy API: The Subscriptions API manages subscriptions for CLI and registry events
    /docs - The Speakeasy Platform Documentation
    """

    auth: Auth
    r"""REST APIs for managing Authentication"""
    github: Github
    r"""REST APIs for managing the github integration"""
    organizations: Organizations
    r"""REST APIs for managing Organizations (speakeasy L1 Tenancy construct)"""
    workspaces: Workspaces
    r"""REST APIs for managing Workspaces (speakeasy tenancy)"""
    events: Events
    r"""REST APIs for managing events captured by a speakeasy binary (CLI, GitHub Action etc)"""
    reports: Reports
    r"""REST APIs for managing reports (lint reports, change reports, etc)"""
    suggest: Suggest
    r"""REST APIs for managing LLM OAS suggestions"""
    short_ur_ls: ShortURLs
    r"""REST APIs for managing short URLs"""
    artifacts: Artifacts
    r"""REST APIs for working with Registry artifacts"""
    subscriptions: Subscriptions
    r"""REST APIs for managing subscriptions"""

    def __init__(
        self,
        security: Optional[
            Union[models.Security, Callable[[], models.Security]]
        ] = None,
        workspace_id: Optional[str] = None,
        server: Optional[str] = None,
        server_url: Optional[str] = None,
        url_params: Optional[Dict[str, str]] = None,
        client: Optional[HttpClient] = None,
        async_client: Optional[AsyncHttpClient] = None,
        retry_config: OptionalNullable[RetryConfig] = UNSET,
        timeout_ms: Optional[int] = None,
        debug_logger: Optional[Logger] = None,
    ) -> None:
        r"""Instantiates the SDK configuring it with the provided parameters.

        :param security: The security details required for authentication
        :param workspace_id: Configures the workspace_id parameter for all supported operations
        :param server: The server by name to use for all methods
        :param server_url: The server URL to use for all methods
        :param url_params: Parameters to optionally template the server URL with
        :param client: The HTTP client to use for all synchronous methods
        :param async_client: The Async HTTP client to use for all asynchronous methods
        :param retry_config: The retry configuration to use for all supported methods
        :param timeout_ms: Optional request timeout applied to each operation in milliseconds
        """
        if client is None:
            client = httpx.Client()

        assert issubclass(
            type(client), HttpClient
        ), "The provided client must implement the HttpClient protocol."

        if async_client is None:
            async_client = httpx.AsyncClient()

        if debug_logger is None:
            debug_logger = get_default_logger()

        assert issubclass(
            type(async_client), AsyncHttpClient
        ), "The provided async_client must implement the AsyncHttpClient protocol."

        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        _globals = internal.Globals(
            workspace_id=utils.get_global_from_env(
                workspace_id, "TESTSDK2_WORKSPACE_ID", str
            ),
        )

        BaseSDK.__init__(
            self,
            SDKConfiguration(
                client=client,
                async_client=async_client,
                globals=_globals,
                security=security,
                server_url=server_url,
                server=server,
                retry_config=retry_config,
                timeout_ms=timeout_ms,
                debug_logger=debug_logger,
            ),
        )

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(
            current_server_url, self.sdk_configuration.client
        )
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        # pylint: disable=protected-access
        self.sdk_configuration.__dict__["_hooks"] = hooks

        self._init_sdks()

    def _init_sdks(self):
        self.auth = Auth(self.sdk_configuration)
        self.github = Github(self.sdk_configuration)
        self.organizations = Organizations(self.sdk_configuration)
        self.workspaces = Workspaces(self.sdk_configuration)
        self.events = Events(self.sdk_configuration)
        self.reports = Reports(self.sdk_configuration)
        self.suggest = Suggest(self.sdk_configuration)
        self.short_ur_ls = ShortURLs(self.sdk_configuration)
        self.artifacts = Artifacts(self.sdk_configuration)
        self.subscriptions = Subscriptions(self.sdk_configuration)

    def __enter__(self):
        return self

    async def __aenter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.sdk_configuration.client is not None:
            self.sdk_configuration.client.close()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.sdk_configuration.async_client is not None:
            await self.sdk_configuration.async_client.aclose()

    def generate_code_sample_preview(
        self,
        *,
        languages: List[str],
        schema_file: Union[models.SchemaFile, models.SchemaFileTypedDict],
        package_name: Optional[str] = None,
        sdk_class_name: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        accept_header_override: Optional[GenerateCodeSamplePreviewAcceptEnum] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.GenerateCodeSamplePreviewResponse:
        r"""Generate Code Sample previews from a file and configuration parameters.

        This endpoint generates Code Sample previews from a file and configuration parameters.

        :param languages: A list of languages to generate code samples for
        :param schema_file: The OpenAPI file to be uploaded
        :param package_name: The name of the package
        :param sdk_class_name: The SDK class name
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param accept_header_override: Override the default accept header for this method
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.CodeSampleSchemaInput(
            package_name=package_name,
            sdk_class_name=sdk_class_name,
            languages=languages,
            schema_file=utils.get_pydantic_model(schema_file, models.SchemaFile),
        )

        req = self.build_request(
            method="POST",
            path="/v1/code_sample/preview",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value=accept_header_override.value
            if accept_header_override is not None
            else "application/json;q=1, application/x-yaml;q=0",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request, False, False, "multipart", models.CodeSampleSchemaInput
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="generateCodeSamplePreview",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            stream=True,
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/x-yaml"):
            return http_res
        if utils.match_response(http_res, "200", "application/json"):
            return http_res
        if utils.match_response(http_res, ["4XX", "5XX"], "application/json"):
            http_res_text = utils.stream_to_text(http_res)
            data = utils.unmarshal_json(http_res_text, models.ErrorData)
            raise models.Error(data=data)

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def generate_code_sample_preview_async(
        self,
        *,
        languages: List[str],
        schema_file: Union[models.SchemaFile, models.SchemaFileTypedDict],
        package_name: Optional[str] = None,
        sdk_class_name: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        accept_header_override: Optional[GenerateCodeSamplePreviewAcceptEnum] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.GenerateCodeSamplePreviewResponse:
        r"""Generate Code Sample previews from a file and configuration parameters.

        This endpoint generates Code Sample previews from a file and configuration parameters.

        :param languages: A list of languages to generate code samples for
        :param schema_file: The OpenAPI file to be uploaded
        :param package_name: The name of the package
        :param sdk_class_name: The SDK class name
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param accept_header_override: Override the default accept header for this method
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.CodeSampleSchemaInput(
            package_name=package_name,
            sdk_class_name=sdk_class_name,
            languages=languages,
            schema_file=utils.get_pydantic_model(schema_file, models.SchemaFile),
        )

        req = self.build_request_async(
            method="POST",
            path="/v1/code_sample/preview",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value=accept_header_override.value
            if accept_header_override is not None
            else "application/json;q=1, application/x-yaml;q=0",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request, False, False, "multipart", models.CodeSampleSchemaInput
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="generateCodeSamplePreview",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            stream=True,
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/x-yaml"):
            return http_res
        if utils.match_response(http_res, "200", "application/json"):
            return http_res
        if utils.match_response(http_res, ["4XX", "5XX"], "application/json"):
            http_res_text = await utils.stream_to_text_async(http_res)
            data = utils.unmarshal_json(http_res_text, models.ErrorData)
            raise models.Error(data=data)

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    def generate_code_sample_preview(
        self,
        *,
        languages: List[str],
        schema_file: Union[models.SchemaFile, models.SchemaFileTypedDict],
        package_name: Optional[str] = None,
        sdk_class_name: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.GenerateCodeSamplePreviewAsyncResponseBody:
        r"""Initiate asynchronous Code Sample preview generation from a file and configuration parameters, receiving an JobID response for polling.

        This endpoint generates Code Sample previews from a file and configuration parameters, receiving an JobID response for polling.

        :param languages: A list of languages to generate code samples for
        :param schema_file: The OpenAPI file to be uploaded
        :param package_name: The name of the package
        :param sdk_class_name: The SDK class name
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.CodeSampleSchemaInput(
            package_name=package_name,
            sdk_class_name=sdk_class_name,
            languages=languages,
            schema_file=utils.get_pydantic_model(schema_file, models.SchemaFile),
        )

        req = self.build_request(
            method="POST",
            path="/v1/code_sample/preview/async",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request, False, False, "multipart", models.CodeSampleSchemaInput
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="generateCodeSamplePreviewAsync",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "202", "application/json"):
            return utils.unmarshal_json(
                http_res.text, models.GenerateCodeSamplePreviewAsyncResponseBody
            )
        if utils.match_response(http_res, ["4XX", "5XX"], "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrorData)
            raise models.Error(data=data)

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def generate_code_sample_preview_async_async(
        self,
        *,
        languages: List[str],
        schema_file: Union[models.SchemaFile, models.SchemaFileTypedDict],
        package_name: Optional[str] = None,
        sdk_class_name: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.GenerateCodeSamplePreviewAsyncResponseBody:
        r"""Initiate asynchronous Code Sample preview generation from a file and configuration parameters, receiving an async JobID response for polling.

        This endpoint generates Code Sample previews from a file and configuration parameters, receiving an async JobID response for polling.

        :param languages: A list of languages to generate code samples for
        :param schema_file: The OpenAPI file to be uploaded
        :param package_name: The name of the package
        :param sdk_class_name: The SDK class name
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.CodeSampleSchemaInput(
            package_name=package_name,
            sdk_class_name=sdk_class_name,
            languages=languages,
            schema_file=utils.get_pydantic_model(schema_file, models.SchemaFile),
        )

        req = self.build_request_async(
            method="POST",
            path="/v1/code_sample/preview/async",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request, False, False, "multipart", models.CodeSampleSchemaInput
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="generateCodeSamplePreviewAsync",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "202", "application/json"):
            return utils.unmarshal_json(
                http_res.text, models.GenerateCodeSamplePreviewAsyncResponseBody
            )
        if utils.match_response(http_res, ["4XX", "5XX"], "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrorData)
            raise models.Error(data=data)

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    def get_code_sample_preview(
        self,
        *,
        job_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        accept_header_override: Optional[GetCodeSamplePreviewAsyncAcceptEnum] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.GetCodeSamplePreviewAsyncResponse:
        r"""Poll for the result of an asynchronous Code Sample preview generation.

        Poll for the result of an asynchronous Code Sample preview generation.

        :param job_id: The ID of the job to check the status and retrieve results
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param accept_header_override: Override the default accept header for this method
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.GetCodeSamplePreviewAsyncRequest(
            job_id=job_id,
        )

        req = self.build_request(
            method="GET",
            path="/v1/code_sample/preview/async/{jobID}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value=accept_header_override.value
            if accept_header_override is not None
            else "application/json;q=1, application/x-yaml;q=0",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="getCodeSamplePreviewAsync",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            stream=True,
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/x-yaml"):
            return http_res
        if utils.match_response(http_res, "200", "application/json"):
            return http_res
        if utils.match_response(http_res, "202", "application/json"):
            http_response_text = utils.stream_to_text(http_res)
            return utils.unmarshal_json(
                http_response_text, models.GetCodeSamplePreviewAsyncResponseBody
            )
        if utils.match_response(http_res, ["4XX", "5XX"], "application/json"):
            http_res_text = utils.stream_to_text(http_res)
            data = utils.unmarshal_json(http_res_text, models.ErrorData)
            raise models.Error(data=data)

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def get_code_sample_preview_async_async(
        self,
        *,
        job_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        accept_header_override: Optional[GetCodeSamplePreviewAsyncAcceptEnum] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.GetCodeSamplePreviewAsyncResponse:
        r"""Poll for the result of an asynchronous Code Sample preview generation.

        Poll for the result of an asynchronous Code Sample preview generation.

        :param job_id: The ID of the job to check the status and retrieve results
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param accept_header_override: Override the default accept header for this method
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.GetCodeSamplePreviewAsyncRequest(
            job_id=job_id,
        )

        req = self.build_request_async(
            method="GET",
            path="/v1/code_sample/preview/async/{jobID}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value=accept_header_override.value
            if accept_header_override is not None
            else "application/json;q=1, application/x-yaml;q=0",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="getCodeSamplePreviewAsync",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            stream=True,
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/x-yaml"):
            return http_res
        if utils.match_response(http_res, "200", "application/json"):
            return http_res
        if utils.match_response(http_res, "202", "application/json"):
            http_response_text = await utils.stream_to_text_async(http_res)
            return utils.unmarshal_json(
                http_response_text, models.GetCodeSamplePreviewAsyncResponseBody
            )
        if utils.match_response(http_res, ["4XX", "5XX"], "application/json"):
            http_res_text = await utils.stream_to_text_async(http_res)
            data = utils.unmarshal_json(http_res_text, models.ErrorData)
            raise models.Error(data=data)

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )
