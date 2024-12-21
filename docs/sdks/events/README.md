# Events
(*events*)

## Overview

REST APIs for managing events captured by a speakeasy binary (CLI, GitHub Action etc)

### Available Operations

* [search](#search) - Search events for a particular workspace by any field
* [post](#post) - Post events for a specific workspace
* [get_events_by_target](#get_events_by_target) - Load recent events for a particular workspace
* [get_targets](#get_targets) - Load targets for a particular workspace
* [get_targets_deprecated](#get_targets_deprecated) - Load targets for a particular workspace

## search

Search events for a particular workspace by any field

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

    res = test_sdk2.events.search()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `workspace_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Unique identifier of the workspace.                                 |
| `source_revision_digest`                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Unique identifier of the source revision digest.                    |
| `lint_report_digest`                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Unique identifier of the lint report digest.                        |
| `openapi_diff_report_digest`                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Unique identifier of the openapi diff report digest.                |
| `interaction_type`                                                  | [Optional[models.InteractionType]](../../models/interactiontype.md) | :heavy_minus_sign:                                                  | Specified interaction type for events.                              |
| `generate_gen_lock_id`                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A specific gen lock ID for the events.                              |
| `execution_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Shared execution ID for cli events across a single action.          |
| `success`                                                           | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Whether the event was successful or not.                            |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Number of results to return.                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.CliEvent]](../../models/.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 5XX              | application/json |
| models.APIError  | 4XX              | \*/\*            |

## post

Sends an array of events to be stored for a particular workspace.

### Example Usage

```python
import dateutil.parser
import os
import test_sdk_package
from test_sdk_package import TestSdk2

with TestSdk2(
    security=test_sdk_package.Security(
        api_key=os.getenv("TESTSDK2_API_KEY", ""),
    ),
) as test_sdk2:

    test_sdk2.events.post(request_body=[
        {
            "id": "<id>",
            "execution_id": "<id>",
            "workspace_id": "<id>",
            "speakeasy_api_key_name": "<value>",
            "interaction_type": test_sdk_package.InteractionType.QUICKSTART,
            "local_started_at": dateutil.parser.isoparse("2023-09-09T05:59:33.876Z"),
            "created_at": dateutil.parser.isoparse("2024-08-12T17:54:17.538Z"),
            "speakeasy_version": "<value>",
            "success": True,
        },
    ])

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request_body`                                                      | List[[models.CliEvent](../../models/clievent.md)]                   | :heavy_check_mark:                                                  | N/A                                                                 |
| `workspace_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Unique identifier of the workspace.                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 5XX              | application/json |
| models.APIError  | 4XX              | \*/\*            |

## get_events_by_target

Load recent events for a particular workspace

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

    res = test_sdk2.events.get_events_by_target(target_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `target_id`                                                                                                       | *str*                                                                                                             | :heavy_check_mark:                                                                                                | Filter to only return events corresponding to a particular gen_lock_id (gen_lock_id uniquely identifies a target) |
| `workspace_id`                                                                                                    | *Optional[str]*                                                                                                   | :heavy_minus_sign:                                                                                                | Unique identifier of the workspace.                                                                               |
| `after_created_at`                                                                                                | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                              | :heavy_minus_sign:                                                                                                | Filter to only return events created after this timestamp                                                         |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |

### Response

**[List[models.CliEvent]](../../models/.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 5XX              | application/json |
| models.APIError  | 4XX              | \*/\*            |

## get_targets

Load targets for a particular workspace

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

    res = test_sdk2.events.get_targets()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `after_last_event_created_at`                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects)   | :heavy_minus_sign:                                                     | Filter to only return targets with events created after this timestamp |
| `retries`                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)       | :heavy_minus_sign:                                                     | Configuration to override the default retry behavior of the client.    |

### Response

**[List[models.TargetSDK]](../../models/.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 5XX              | application/json |
| models.APIError  | 4XX              | \*/\*            |

## get_targets_deprecated

Load targets for a particular workspace

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

    res = test_sdk2.events.get_targets_deprecated()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `workspace_id`                                                         | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | Unique identifier of the workspace.                                    |
| `after_last_event_created_at`                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects)   | :heavy_minus_sign:                                                     | Filter to only return targets with events created after this timestamp |
| `retries`                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)       | :heavy_minus_sign:                                                     | Configuration to override the default retry behavior of the client.    |

### Response

**[List[models.TargetSDK]](../../models/.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 5XX              | application/json |
| models.APIError  | 4XX              | \*/\*            |