# test-sdk-package

Developer-friendly & type-safe Python SDK specifically catered to leverage *test-sdk-package* API.

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=test-sdk-package&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


<br /><br />
> [!IMPORTANT]
> This SDK is not yet ready for production use. To complete setup please follow the steps outlined in your [workspace](https://app.speakeasy.com/org/test-company-2/ws-3). Delete this section before > publishing to a package manager.

<!-- Start Summary [summary] -->
## Summary

Speakeasy API: The Subscriptions API manages subscriptions for CLI and registry events

For more information about the API: [The Speakeasy Platform Documentation](/docs)
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [test-sdk-package](#test-sdk-package)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Global Parameters](#global-parameters)
  * [File uploads](#file-uploads)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Debugging](#debugging)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!TIP]
> To finish publishing your SDK to PyPI you must [run your first generation action](https://www.speakeasy.com/docs/github-setup#step-by-step-guide).


The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install git+<UNSET>.git
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add git+<UNSET>.git
```
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
import os
import test_sdk_package
from test_sdk_package import TestSdk2

with TestSdk2(
    security=test_sdk_package.Security(
        api_key=os.getenv("TESTSDK2_API_KEY", ""),
    ),
) as test_sdk2:

    res = test_sdk2.generate_code_sample_preview(languages=[
        "<value>",
        "<value>",
    ], schema_file={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    })

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import os
import test_sdk_package
from test_sdk_package import TestSdk2

async def main():
    async with TestSdk2(
        security=test_sdk_package.Security(
            api_key=os.getenv("TESTSDK2_API_KEY", ""),
        ),
    ) as test_sdk2:

        res = await test_sdk2.generate_code_sample_preview_async(languages=[
            "<value>",
            "<value>",
        ], schema_file={
            "file_name": "example.file",
            "content": open("example.file", "rb"),
        })

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security schemes globally:

| Name                   | Type   | Scheme      | Environment Variable            |
| ---------------------- | ------ | ----------- | ------------------------------- |
| `api_key`              | apiKey | API key     | `TESTSDK2_API_KEY`              |
| `workspace_identifier` | apiKey | API key     | `TESTSDK2_WORKSPACE_IDENTIFIER` |
| `bearer`               | http   | HTTP Bearer | `TESTSDK2_BEARER`               |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. The selected scheme will be used by default to authenticate with the API for all operations that support it. For example:
```python
import os
import test_sdk_package
from test_sdk_package import TestSdk2

with TestSdk2(
    security=test_sdk_package.Security(
        api_key=os.getenv("TESTSDK2_API_KEY", ""),
    ),
) as test_sdk2:

    res = test_sdk2.generate_code_sample_preview(languages=[
        "<value>",
        "<value>",
    ], schema_file={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    })

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [artifacts](docs/sdks/artifacts/README.md)

* [preflight](docs/sdks/artifacts/README.md#preflight) - Get access token for communicating with OCI distribution endpoints
* [get_namespaces](docs/sdks/artifacts/README.md#get_namespaces) - Each namespace contains many revisions.
* [get_revisions](docs/sdks/artifacts/README.md#get_revisions)
* [get_tags](docs/sdks/artifacts/README.md#get_tags)
* [post_tags](docs/sdks/artifacts/README.md#post_tags) - Add tags to an existing revision
* [set_visibility](docs/sdks/artifacts/README.md#set_visibility) - Set visibility of a namespace with an existing metadata entry
* [list_remote_sources](docs/sdks/artifacts/README.md#list_remote_sources) - Get remote sources attached to a particular namespace
* [create_remote_source](docs/sdks/artifacts/README.md#create_remote_source) - Configure a new remote source
* [get_manifest](docs/sdks/artifacts/README.md#get_manifest) - Get manifest for a particular reference
* [get_blob](docs/sdks/artifacts/README.md#get_blob) - Get blob for a particular digest

### [auth](docs/sdks/auth/README.md)

* [validate_api_key](docs/sdks/auth/README.md#validate_api_key) - Validate the current api key.
* [get_user](docs/sdks/auth/README.md#get_user) - Get information about the current user.
* [get_access_token](docs/sdks/auth/README.md#get_access_token) - Get or refresh an access token for the current workspace.
* [get_access](docs/sdks/auth/README.md#get_access) - Get access allowances for a particular workspace

### [events](docs/sdks/events/README.md)

* [search](docs/sdks/events/README.md#search) - Search events for a particular workspace by any field
* [post](docs/sdks/events/README.md#post) - Post events for a specific workspace
* [get_events_by_target](docs/sdks/events/README.md#get_events_by_target) - Load recent events for a particular workspace
* [get_targets](docs/sdks/events/README.md#get_targets) - Load targets for a particular workspace
* [get_targets_deprecated](docs/sdks/events/README.md#get_targets_deprecated) - Load targets for a particular workspace

### [github](docs/sdks/github/README.md)

* [get_setup](docs/sdks/github/README.md#get_setup)
* [check_access](docs/sdks/github/README.md#check_access)
* [link_github](docs/sdks/github/README.md#link_github)
* [check_publishing_p_rs](docs/sdks/github/README.md#check_publishing_p_rs)
* [check_publishing_secrets](docs/sdks/github/README.md#check_publishing_secrets)
* [store_publishing_secrets](docs/sdks/github/README.md#store_publishing_secrets)
* [configure_code_samples](docs/sdks/github/README.md#configure_code_samples)
* [configure_mintlify_repo](docs/sdks/github/README.md#configure_mintlify_repo)
* [configure_target](docs/sdks/github/README.md#configure_target)
* [trigger_action](docs/sdks/github/README.md#trigger_action)
* [get_action](docs/sdks/github/README.md#get_action)

### [organizations](docs/sdks/organizations/README.md)

* [get_all](docs/sdks/organizations/README.md#get_all) - Get organizations for a user
* [create](docs/sdks/organizations/README.md#create) - Create an organization
* [get](docs/sdks/organizations/README.md#get) - Get organization
* [create_free_trial](docs/sdks/organizations/README.md#create_free_trial) - Create a free trial for an organization
* [get_usage](docs/sdks/organizations/README.md#get_usage) - Get billing usage summary for a particular organization

### [reports](docs/sdks/reports/README.md)

* [upload_report](docs/sdks/reports/README.md#upload_report) - Upload a report.
* [get_linting_report_signed_url](docs/sdks/reports/README.md#get_linting_report_signed_url) - Get the signed access url for the linting reports for a particular document.
* [get_changes_report_signed_url](docs/sdks/reports/README.md#get_changes_report_signed_url) - Get the signed access url for the change reports for a particular document.

### [short_ur_ls](docs/sdks/shorturls/README.md)

* [create](docs/sdks/shorturls/README.md#create) - Shorten a URL.

### [subscriptions](docs/sdks/subscriptions/README.md)

* [ignore_subscription_namespace](docs/sdks/subscriptions/README.md#ignore_subscription_namespace) - Ignored a namespace for a subscription
* [activate_subscription_namespace](docs/sdks/subscriptions/README.md#activate_subscription_namespace) - Activate an ignored namespace for a subscription

### [suggest](docs/sdks/suggest/README.md)

* [suggest_open_api](docs/sdks/suggest/README.md#suggest_open_api) - (DEPRECATED) Generate suggestions for improving an OpenAPI document.
* [suggest](docs/sdks/suggest/README.md#suggest) - Generate suggestions for improving an OpenAPI document.
* [suggest_items](docs/sdks/suggest/README.md#suggest_items) - Generate generic suggestions for a list of items.
* [suggest_open_api_registry](docs/sdks/suggest/README.md#suggest_open_api_registry) - Generate suggestions for improving an OpenAPI document stored in the registry.

### [TestSdk2 SDK](docs/sdks/testsdk2/README.md)

* [generate_code_sample_preview](docs/sdks/testsdk2/README.md#generate_code_sample_preview) - Generate Code Sample previews from a file and configuration parameters.
* [generate_code_sample_preview_async](docs/sdks/testsdk2/README.md#generate_code_sample_preview_async) - Initiate asynchronous Code Sample preview generation from a file and configuration parameters, receiving an async JobID response for polling.
* [get_code_sample_preview_async](docs/sdks/testsdk2/README.md#get_code_sample_preview_async) - Poll for the result of an asynchronous Code Sample preview generation.

### [workspaces](docs/sdks/workspaces/README.md)

* [get_all](docs/sdks/workspaces/README.md#get_all) - Get workspaces for a user
* [get](docs/sdks/workspaces/README.md#get) - Get workspace by context
* [create](docs/sdks/workspaces/README.md#create) - Create a workspace
* [get_by_id](docs/sdks/workspaces/README.md#get_by_id) - Get workspace
* [update](docs/sdks/workspaces/README.md#update) - Update workspace details
* [get_settings](docs/sdks/workspaces/README.md#get_settings) - Get workspace settings
* [update_settings](docs/sdks/workspaces/README.md#update_settings) - Update workspace settings
* [get_team](docs/sdks/workspaces/README.md#get_team) - Get team members for a particular workspace
* [grant_access](docs/sdks/workspaces/README.md#grant_access) - Grant a user access to a particular workspace
* [revoke_access](docs/sdks/workspaces/README.md#revoke_access) - Revoke a user's access to a particular workspace
* [get_tokens](docs/sdks/workspaces/README.md#get_tokens) - Get tokens for a particular workspace
* [create_token](docs/sdks/workspaces/README.md#create_token) - Create a token for a particular workspace
* [delete_token](docs/sdks/workspaces/README.md#delete_token) - Delete a token for a particular workspace
* [get_feature_flags](docs/sdks/workspaces/README.md#get_feature_flags) - Get workspace feature flags

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Global Parameters [global-parameters] -->
## Global Parameters

A parameter is configured globally. This parameter may be set on the SDK client instance itself during initialization. When configured as an option during SDK initialization, This global value will be used as the default on the operations that use it. When such operations are called, there is a place in each to override the global value, if needed.

For example, you can set `workspace_id` to `"<id>"` at SDK initialization and then you do not have to pass the same value on calls to operations like `get_access_token`. But if you want to do so you may, which will locally override the global setting. See the example code below for a demonstration.


### Available Globals

The following global parameter is available.
Global parameters can also be set via environment variable.

| Name         | Type | Description                 | Environment           |
| ------------ | ---- | --------------------------- | --------------------- |
| workspace_id | str  | The workspace_id parameter. | TESTSDK2_WORKSPACE_ID |

### Example

```python
from test_sdk_package import TestSdk2

with TestSdk2() as test_sdk2:

    res = test_sdk2.auth.get_access_token(workspace_id="<id>")

    # Handle response
    print(res)

```
<!-- End Global Parameters [global-parameters] -->

<!-- Start File uploads [file-upload] -->
## File uploads

Certain SDK methods accept file objects as part of a request body or multi-part request. It is possible and typically recommended to upload files as a stream rather than reading the entire contents into memory. This avoids excessive memory consumption and potentially crashing with out-of-memory errors when working with very large files. The following example demonstrates how to attach a file stream to a request.

> [!TIP]
>
> For endpoints that handle file uploads bytes arrays can also be used. However, using streams is recommended for large files.
>

```python
import os
import test_sdk_package
from test_sdk_package import TestSdk2

with TestSdk2(
    security=test_sdk_package.Security(
        api_key=os.getenv("TESTSDK2_API_KEY", ""),
    ),
) as test_sdk2:

    res = test_sdk2.generate_code_sample_preview(languages=[
        "<value>",
        "<value>",
    ], schema_file={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    })

    # Handle response
    print(res)

```
<!-- End File uploads [file-upload] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
import os
import test_sdk_package
from test_sdk_package import TestSdk2
from test_sdk_package.utils import BackoffStrategy, RetryConfig

with TestSdk2(
    security=test_sdk_package.Security(
        api_key=os.getenv("TESTSDK2_API_KEY", ""),
    ),
) as test_sdk2:

    res = test_sdk2.generate_code_sample_preview(languages=[
        "<value>",
        "<value>",
    ], schema_file={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    },
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
import os
import test_sdk_package
from test_sdk_package import TestSdk2
from test_sdk_package.utils import BackoffStrategy, RetryConfig

with TestSdk2(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    security=test_sdk_package.Security(
        api_key=os.getenv("TESTSDK2_API_KEY", ""),
    ),
) as test_sdk2:

    res = test_sdk2.generate_code_sample_preview(languages=[
        "<value>",
        "<value>",
    ], schema_file={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    })

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a models.APIError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `generate_code_sample_preview_async` method may raise the following exceptions:

| Error Type   | Status Code | Content Type     |
| ------------ | ----------- | ---------------- |
| models.Error | 4XX, 5XX    | application/json |

### Example

```python
import os
import test_sdk_package
from test_sdk_package import TestSdk2, models

with TestSdk2(
    security=test_sdk_package.Security(
        api_key=os.getenv("TESTSDK2_API_KEY", ""),
    ),
) as test_sdk2:
    res = None
    try:

        res = test_sdk2.generate_code_sample_preview(languages=[
            "<value>",
            "<value>",
        ], schema_file={
            "file_name": "example.file",
            "content": open("example.file", "rb"),
        })

        # Handle response
        print(res)

    except models.Error as e:
        # handle e.data: models.ErrorData
        raise(e)
    except models.APIError as e:
        # handle exception
        raise(e)
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Name

You can override the default server globally by passing a server name to the `server: str` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the names associated with the available servers:

| Name   | Server                              |
| ------ | ----------------------------------- |
| `prod` | `https://api.prod.speakeasyapi.dev` |

#### Example

```python
import os
import test_sdk_package
from test_sdk_package import TestSdk2

with TestSdk2(
    server="prod",
    security=test_sdk_package.Security(
        api_key=os.getenv("TESTSDK2_API_KEY", ""),
    ),
) as test_sdk2:

    res = test_sdk2.generate_code_sample_preview(languages=[
        "<value>",
        "<value>",
    ], schema_file={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    })

    # Handle response
    print(res)

```

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import os
import test_sdk_package
from test_sdk_package import TestSdk2

with TestSdk2(
    server_url="https://api.prod.speakeasyapi.dev",
    security=test_sdk_package.Security(
        api_key=os.getenv("TESTSDK2_API_KEY", ""),
    ),
) as test_sdk2:

    res = test_sdk2.generate_code_sample_preview(languages=[
        "<value>",
        "<value>",
    ], schema_file={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    })

    # Handle response
    print(res)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from test_sdk_package import TestSdk2
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = TestSdk2(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from test_sdk_package import TestSdk2
from test_sdk_package.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = TestSdk2(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from test_sdk_package import TestSdk2
import logging

logging.basicConfig(level=logging.DEBUG)
s = TestSdk2(debug_logger=logging.getLogger("test_sdk_package"))
```

You can also enable a default debug logger by setting an environment variable `TESTSDK2_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=test-sdk-package&utm_campaign=python)
test
