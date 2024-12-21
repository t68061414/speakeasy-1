# Artifacts
(*artifacts*)

## Overview

REST APIs for working with Registry artifacts

### Available Operations

* [preflight](#preflight) - Get access token for communicating with OCI distribution endpoints
* [get_namespaces](#get_namespaces) - Each namespace contains many revisions.
* [get_revisions](#get_revisions)
* [get_tags](#get_tags)
* [post_tags](#post_tags) - Add tags to an existing revision
* [set_visibility](#set_visibility) - Set visibility of a namespace with an existing metadata entry
* [list_remote_sources](#list_remote_sources) - Get remote sources attached to a particular namespace
* [create_remote_source](#create_remote_source) - Configure a new remote source
* [get_manifest](#get_manifest) - Get manifest for a particular reference
* [get_blob](#get_blob) - Get blob for a particular digest

## preflight

Get access token for communicating with OCI distribution endpoints

### Example Usage

```python
import os
import test_sdk_package
from test_sdk_package import TestSdk2

with TestSdk2(
    security=test_sdk_package.Security(
        api_key=os.getenv("TESTSDK2_API_KEY", ""),
    ),
) as test_sdk2:

    res = test_sdk2.artifacts.preflight()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.PreflightRequest](../../models/preflightrequest.md)         | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PreflightToken](../../models/preflighttoken.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 4XX              | application/json |
| models.APIError  | 5XX              | \*/\*            |

## get_namespaces

Each namespace contains many revisions.

### Example Usage

```python
import os
import test_sdk_package
from test_sdk_package import TestSdk2

with TestSdk2(
    security=test_sdk_package.Security(
        api_key=os.getenv("TESTSDK2_API_KEY", ""),
    ),
) as test_sdk2:

    res = test_sdk2.artifacts.get_namespaces()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetNamespacesResponse](../../models/getnamespacesresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 4XX              | application/json |
| models.APIError  | 5XX              | \*/\*            |

## get_revisions

### Example Usage

```python
import os
import test_sdk_package
from test_sdk_package import TestSdk2

with TestSdk2(
    security=test_sdk_package.Security(
        api_key=os.getenv("TESTSDK2_API_KEY", ""),
    ),
) as test_sdk2:

    res = test_sdk2.artifacts.get_revisions(namespace_name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `namespace_name`                                                    | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `next_page_token`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Token to retrieve the next page of results                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetRevisionsResponse](../../models/getrevisionsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 4XX              | application/json |
| models.APIError  | 5XX              | \*/\*            |

## get_tags

### Example Usage

```python
import os
import test_sdk_package
from test_sdk_package import TestSdk2

with TestSdk2(
    security=test_sdk_package.Security(
        api_key=os.getenv("TESTSDK2_API_KEY", ""),
    ),
) as test_sdk2:

    res = test_sdk2.artifacts.get_tags(namespace_name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `namespace_name`                                                    | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetTagsResponse](../../models/gettagsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 4XX              | application/json |
| models.APIError  | 5XX              | \*/\*            |

## post_tags

Add tags to an existing revision

### Example Usage

```python
import os
import test_sdk_package
from test_sdk_package import TestSdk2

with TestSdk2(
    security=test_sdk_package.Security(
        api_key=os.getenv("TESTSDK2_API_KEY", ""),
    ),
) as test_sdk2:

    test_sdk2.artifacts.post_tags(namespace_name="<value>", revision_digest="<value>", tags=[
        "<value>",
    ])

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `namespace_name`                                                    | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `revision_digest`                                                   | *str*                                                               | :heavy_check_mark:                                                  | revision digest to add tags too sha256:...                          |
| `tags`                                                              | List[*str*]                                                         | :heavy_check_mark:                                                  | string tags to add to the revision                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 4XX              | application/json |
| models.APIError  | 5XX              | \*/\*            |

## set_visibility

Set visibility of a namespace with an existing metadata entry

### Example Usage

```python
import os
import test_sdk_package
from test_sdk_package import TestSdk2

with TestSdk2(
    security=test_sdk_package.Security(
        api_key=os.getenv("TESTSDK2_API_KEY", ""),
    ),
) as test_sdk2:

    test_sdk2.artifacts.set_visibility(namespace_name="<value>", public=False)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `namespace_name`                                                    | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `public`                                                            | *bool*                                                              | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 4XX              | application/json |
| models.APIError  | 5XX              | \*/\*            |

## list_remote_sources

Get remote sources attached to a particular namespace

### Example Usage

```python
import os
import test_sdk_package
from test_sdk_package import TestSdk2

with TestSdk2(
    security=test_sdk_package.Security(
        api_key=os.getenv("TESTSDK2_API_KEY", ""),
    ),
) as test_sdk2:

    res = test_sdk2.artifacts.list_remote_sources(namespace_name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `namespace_name`                                                    | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RemoteSource](../../models/remotesource.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 4XX              | application/json |
| models.APIError  | 5XX              | \*/\*            |

## create_remote_source

Configure a new remote source

### Example Usage

```python
import os
import test_sdk_package
from test_sdk_package import TestSdk2

with TestSdk2(
    security=test_sdk_package.Security(
        api_key=os.getenv("TESTSDK2_API_KEY", ""),
    ),
) as test_sdk2:

    test_sdk2.artifacts.create_remote_source()

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.RemoteSource](../../models/remotesource.md)                 | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 4XX              | application/json |
| models.APIError  | 5XX              | \*/\*            |

## get_manifest

Get manifest for a particular reference

### Example Usage

```python
import os
import test_sdk_package
from test_sdk_package import TestSdk2

with TestSdk2(
    security=test_sdk_package.Security(
        api_key=os.getenv("TESTSDK2_API_KEY", ""),
    ),
) as test_sdk2:

    res = test_sdk2.artifacts.get_manifest(organization_slug="<value>", workspace_slug="<value>", namespace_name="<value>", revision_reference="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_slug`                                                 | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `workspace_slug`                                                    | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `namespace_name`                                                    | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `revision_reference`                                                | *str*                                                               | :heavy_check_mark:                                                  | Tag or digest                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Manifest](../../models/manifest.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 4XX              | application/json |
| models.APIError  | 5XX              | \*/\*            |

## get_blob

Get blob for a particular digest

### Example Usage

```python
import os
import test_sdk_package
from test_sdk_package import TestSdk2

with TestSdk2(
    security=test_sdk_package.Security(
        api_key=os.getenv("TESTSDK2_API_KEY", ""),
    ),
) as test_sdk2:

    res = test_sdk2.artifacts.get_blob(organization_slug="<value>", workspace_slug="<value>", namespace_name="<value>", digest="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_slug`                                                 | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `workspace_slug`                                                    | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `namespace_name`                                                    | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `digest`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[httpx.Response](../../models/.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 4XX              | application/json |
| models.APIError  | 5XX              | \*/\*            |