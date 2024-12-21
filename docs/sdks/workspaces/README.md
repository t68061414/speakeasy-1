# Workspaces
(*workspaces*)

## Overview

REST APIs for managing Workspaces (speakeasy tenancy)

### Available Operations

* [get_all](#get_all) - Get workspaces for a user
* [get](#get) - Get workspace by context
* [create](#create) - Create a workspace
* [get_by_id](#get_by_id) - Get workspace
* [update](#update) - Update workspace details
* [get_settings](#get_settings) - Get workspace settings
* [update_settings](#update_settings) - Update workspace settings
* [get_team](#get_team) - Get team members for a particular workspace
* [grant_access](#grant_access) - Grant a user access to a particular workspace
* [revoke_access](#revoke_access) - Revoke a user's access to a particular workspace
* [get_tokens](#get_tokens) - Get tokens for a particular workspace
* [create_token](#create_token) - Create a token for a particular workspace
* [delete_token](#delete_token) - Delete a token for a particular workspace
* [get_feature_flags](#get_feature_flags) - Get workspace feature flags

## get_all

Returns a list of workspaces a user has access too

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

    res = test_sdk2.workspaces.get_all()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.Workspace]](../../models/.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 4XX              | application/json |
| models.APIError  | 5XX              | \*/\*            |

## get

Get information about a particular workspace by context.

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

    res = test_sdk2.workspaces.get()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.WorkspaceAndOrganization](../../models/workspaceandorganization.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 4XX              | application/json |
| models.APIError  | 5XX              | \*/\*            |

## create

Creates a workspace

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

    res = test_sdk2.workspaces.create(created_at=dateutil.parser.isoparse("2023-06-18T07:14:55.338Z"), id="<id>", name="<value>", organization_id="<id>", slug="<value>", updated_at=dateutil.parser.isoparse("2023-12-01T17:06:07.804Z"), verified=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                         | Type                                                                                                                                                                              | Required                                                                                                                                                                          | Description                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `created_at`                                                                                                                                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                              | :heavy_check_mark:                                                                                                                                                                | N/A                                                                                                                                                                               |
| `id`                                                                                                                                                                              | *str*                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                | N/A                                                                                                                                                                               |
| `name`                                                                                                                                                                            | *str*                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                | N/A                                                                                                                                                                               |
| `organization_id`                                                                                                                                                                 | *str*                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                | N/A                                                                                                                                                                               |
| `slug`                                                                                                                                                                            | *str*                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                | N/A                                                                                                                                                                               |
| `updated_at`                                                                                                                                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                              | :heavy_check_mark:                                                                                                                                                                | N/A                                                                                                                                                                               |
| `verified`                                                                                                                                                                        | *bool*                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                | N/A                                                                                                                                                                               |
| `inactive`                                                                                                                                                                        | *Optional[bool]*                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                | N/A                                                                                                                                                                               |
| `telemetry_disabled`                                                                                                                                                              | *Optional[bool]*                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                | : warning: ** DEPRECATED **: This will be removed in a future release, please migrate away from it as soon as possible.<br/><br/>Deprecated. Use organization.telemetry_disabled instead. |
| `retries`                                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                                               |

### Response

**[models.Workspace](../../models/workspace.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 4XX              | application/json |
| models.APIError  | 5XX              | \*/\*            |

## get_by_id

Get information about a particular workspace.

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

    res = test_sdk2.workspaces.get_by_id()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `workspace_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Unique identifier of the workspace.                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Workspace](../../models/workspace.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 4XX              | application/json |
| models.APIError  | 5XX              | \*/\*            |

## update

Update information about a particular workspace.

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

    test_sdk2.workspaces.update(created_at=dateutil.parser.isoparse("2024-07-28T19:04:48.565Z"), id="<id>", name="<value>", organization_id="<id>", slug="<value>", updated_at=dateutil.parser.isoparse("2023-10-17T10:52:42.015Z"), verified=True)

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                         | Type                                                                                                                                                                              | Required                                                                                                                                                                          | Description                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `created_at`                                                                                                                                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                              | :heavy_check_mark:                                                                                                                                                                | N/A                                                                                                                                                                               |
| `id`                                                                                                                                                                              | *str*                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                | N/A                                                                                                                                                                               |
| `name`                                                                                                                                                                            | *str*                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                | N/A                                                                                                                                                                               |
| `organization_id`                                                                                                                                                                 | *str*                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                | N/A                                                                                                                                                                               |
| `slug`                                                                                                                                                                            | *str*                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                | N/A                                                                                                                                                                               |
| `updated_at`                                                                                                                                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                              | :heavy_check_mark:                                                                                                                                                                | N/A                                                                                                                                                                               |
| `verified`                                                                                                                                                                        | *bool*                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                | N/A                                                                                                                                                                               |
| `workspace_id`                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                | Unique identifier of the workspace.                                                                                                                                               |
| `inactive`                                                                                                                                                                        | *Optional[bool]*                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                | N/A                                                                                                                                                                               |
| `telemetry_disabled`                                                                                                                                                              | *Optional[bool]*                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                | : warning: ** DEPRECATED **: This will be removed in a future release, please migrate away from it as soon as possible.<br/><br/>Deprecated. Use organization.telemetry_disabled instead. |
| `retries`                                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                                               |

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 4XX              | application/json |
| models.APIError  | 5XX              | \*/\*            |

## get_settings

Get settings about a particular workspace.

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

    res = test_sdk2.workspaces.get_settings()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `workspace_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Unique identifier of the workspace.                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.WorkspaceSettings](../../models/workspacesettings.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 4XX              | application/json |
| models.APIError  | 5XX              | \*/\*            |

## update_settings

Update settings about a particular workspace.

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

    test_sdk2.workspaces.update_settings(workspace_id="<id>", webhook_url="https://last-suspension.info/", created_at=dateutil.parser.isoparse("2023-12-29T06:46:35.807Z"), updated_at=dateutil.parser.isoparse("2024-02-04T10:37:56.725Z"))

    # Use the SDK ...

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `workspace_id`                                                       | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `webhook_url`                                                        | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `updated_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `workspace_id_param`                                                 | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Unique identifier of the workspace.                                  |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 4XX              | application/json |
| models.APIError  | 5XX              | \*/\*            |

## get_team

Get team members for a particular workspace

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

    res = test_sdk2.workspaces.get_team()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `workspace_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Unique identifier of the workspace.                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.WorkspaceTeamResponse](../../models/workspaceteamresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 4XX              | application/json |
| models.APIError  | 5XX              | \*/\*            |

## grant_access

Grant a user access to a particular workspace

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

    res = test_sdk2.workspaces.grant_access(email="Lucinda.Batz8@hotmail.com")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `email`                                                             | *str*                                                               | :heavy_check_mark:                                                  | Email of the user to grant access to.                               |
| `workspace_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Unique identifier of the workspace.                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.WorkspaceInviteResponse](../../models/workspaceinviteresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 4XX              | application/json |
| models.APIError  | 5XX              | \*/\*            |

## revoke_access

Revoke a user's access to a particular workspace

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

    test_sdk2.workspaces.revoke_access(user_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier of the user.                                      |
| `workspace_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Unique identifier of the workspace.                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 4XX              | application/json |
| models.APIError  | 5XX              | \*/\*            |

## get_tokens

Get tokens for a particular workspace

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

    res = test_sdk2.workspaces.get_tokens()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `workspace_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Unique identifier of the workspace.                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.WorkspaceToken]](../../models/.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 4XX              | application/json |
| models.APIError  | 5XX              | \*/\*            |

## create_token

Create a token for a particular workspace

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

    test_sdk2.workspaces.create_token(id="<id>", name="<value>", workspace_id="<id>", alg="<value>", key="<key>", created_at=dateutil.parser.isoparse("2022-08-16T02:33:00.784Z"))

    # Use the SDK ...

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `name`                                                               | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `workspace_id`                                                       | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `alg`                                                                | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `key`                                                                | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `workspace_id_param`                                                 | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Unique identifier of the workspace.                                  |
| `last_used`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `created_by`                                                         | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | N/A                                                                  |
| `email`                                                              | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | N/A                                                                  |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 4XX              | application/json |
| models.APIError  | 5XX              | \*/\*            |

## delete_token

Delete a token for a particular workspace

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

    test_sdk2.workspaces.delete_token(token_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `token_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier of the token.                                     |
| `workspace_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Unique identifier of the workspace.                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 4XX              | application/json |
| models.APIError  | 5XX              | \*/\*            |

## get_feature_flags

Get workspace feature flags

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

    res = test_sdk2.workspaces.get_feature_flags()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `workspace_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Unique identifier of the workspace.                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.WorkspaceFeatureFlagResponse](../../models/workspacefeatureflagresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 5XX              | application/json |
| models.APIError  | 4XX              | \*/\*            |