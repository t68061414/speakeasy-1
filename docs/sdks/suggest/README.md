# Suggest
(*suggest*)

## Overview

REST APIs for managing LLM OAS suggestions

### Available Operations

* [suggest_open_api](#suggest_open_api) - (DEPRECATED) Generate suggestions for improving an OpenAPI document.
* [suggest](#suggest) - Generate suggestions for improving an OpenAPI document.
* [suggest_items](#suggest_items) - Generate generic suggestions for a list of items.
* [suggest_open_api_registry](#suggest_open_api_registry) - Generate suggestions for improving an OpenAPI document stored in the registry.

## suggest_open_api

Get suggestions from an LLM model for improving an OpenAPI document.

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

    res = test_sdk2.suggest.suggest_open_api(x_session_id="<id>", schema={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `x_session_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `schema_`                                                           | [models.Schema](../../models/schema.md)                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `opts`                                                              | [Optional[models.SuggestOptsOld]](../../models/suggestoptsold.md)   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[httpx.Response](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## suggest

Get suggestions from an LLM model for improving an OpenAPI document.

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

    res = test_sdk2.suggest.suggest(x_session_id="<id>", oas_summary={
        "info": {
            "title": "<value>",
            "summary": "<value>",
            "description": "ugh which garrote ashamed sarong fiddle really",
            "version": "<value>",
            "license": {},
        },
        "operations": [
            {
                "method": "<value>",
                "path": "/rescue",
                "operation_id": "<id>",
                "description": "kielbasa psst stitcher cannon devoted blindly apropos low",
                "tags": [
                    "<value>",
                ],
            },
        ],
    }, suggestion_type=test_sdk_package.SuggestRequestBodySuggestionType.DIAGNOSTICS_ONLY, diagnostics=[
        {
            "message": "<value>",
            "path": [
                "/opt/share",
            ],
            "type": "<value>",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `x_session_id`                                                                              | *str*                                                                                       | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `oas_summary`                                                                               | [models.OASSummary](../../models/oassummary.md)                                             | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `suggestion_type`                                                                           | [models.SuggestRequestBodySuggestionType](../../models/suggestrequestbodysuggestiontype.md) | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `diagnostics`                                                                               | List[[models.Diagnostic](../../models/diagnostic.md)]                                       | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[httpx.Response](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## suggest_items

Generate generic suggestions for a list of items.

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

    res = test_sdk2.suggest.suggest_items(prompt="<value>", items=[
        "<value>",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `prompt`                                                                                                | *str*                                                                                                   | :heavy_check_mark:                                                                                      | The prompt to use for the suggestion. Think of this as the "preamble".                                  |
| `items`                                                                                                 | List[*str*]                                                                                             | :heavy_check_mark:                                                                                      | The list of "things" to get suggestions for. One suggestion will be returned for each item in the list. |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

### Response

**[List[str]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## suggest_open_api_registry

Get suggestions from an LLM model for improving an OpenAPI document stored in the registry.

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

    res = test_sdk2.suggest.suggest_open_api_registry(x_session_id="<id>", namespace_name="<value>", revision_reference="<value>", oas_summary={
        "info": {
            "title": "<value>",
            "summary": "<value>",
            "description": "absentmindedly retract ice-cream ugh epic hence",
            "version": "<value>",
            "license": {},
        },
        "operations": [
            {
                "method": "<value>",
                "path": "/boot",
                "operation_id": "<id>",
                "description": "orderly appertain inasmuch headline carelessly fencing",
                "tags": [
                    "<value>",
                ],
            },
        ],
    }, suggestion_type=test_sdk_package.SuggestRequestBodySuggestionType.METHOD_NAMES, diagnostics=[
        {
            "message": "<value>",
            "path": [
                "/Users",
            ],
            "type": "<value>",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `x_session_id`                                                                              | *str*                                                                                       | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `namespace_name`                                                                            | *str*                                                                                       | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `revision_reference`                                                                        | *str*                                                                                       | :heavy_check_mark:                                                                          | Tag or digest                                                                               |
| `oas_summary`                                                                               | [models.OASSummary](../../models/oassummary.md)                                             | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `suggestion_type`                                                                           | [models.SuggestRequestBodySuggestionType](../../models/suggestrequestbodysuggestiontype.md) | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `diagnostics`                                                                               | List[[models.Diagnostic](../../models/diagnostic.md)]                                       | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[httpx.Response](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |