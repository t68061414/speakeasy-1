# Github
(*github*)

## Overview

REST APIs for managing the github integration

### Available Operations

* [get_setup](#get_setup)
* [check_access](#check_access)
* [link_github](#link_github)
* [check_publishing_p_rs](#check_publishing_p_rs)
* [check_publishing_secrets](#check_publishing_secrets)
* [store_publishing_secrets](#store_publishing_secrets)
* [configure_code_samples](#configure_code_samples)
* [configure_mintlify_repo](#configure_mintlify_repo)
* [configure_target](#configure_target)
* [trigger_action](#trigger_action)
* [get_action](#get_action)

## get_setup

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

    res = test_sdk2.github.get_setup(org="<value>", repo="<value>", generate_gen_lock_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `org`                                                               | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `repo`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `generate_gen_lock_id`                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GithubSetupStateResponse](../../models/githubsetupstateresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 4XX              | application/json |
| models.APIError  | 5XX              | \*/\*            |

## check_access

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

    test_sdk2.github.check_access(org="<value>", repo="<value>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `org`                                                               | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `repo`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 4XX              | application/json |
| models.APIError  | 5XX              | \*/\*            |

## link_github

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

    test_sdk2.github.link_github()

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `installation_id`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `github_org`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `github_oidc_token`                                                 | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 4XX              | application/json |
| models.APIError  | 5XX              | \*/\*            |

## check_publishing_p_rs

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

    res = test_sdk2.github.check_publishing_p_rs(generate_gen_lock_id="<id>", org="<value>", repo="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `generate_gen_lock_id`                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `org`                                                               | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `repo`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GithubPublishingPRResponse](../../models/githubpublishingprresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 4XX              | application/json |
| models.APIError  | 5XX              | \*/\*            |

## check_publishing_secrets

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

    res = test_sdk2.github.check_publishing_secrets(generate_gen_lock_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `generate_gen_lock_id`                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GithubMissingPublishingSecretsResponse](../../models/githubmissingpublishingsecretsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 4XX              | application/json |
| models.APIError  | 5XX              | \*/\*            |

## store_publishing_secrets

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

    test_sdk2.github.store_publishing_secrets(generate_gen_lock_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `generate_gen_lock_id`                                              | *str*                                                               | :heavy_check_mark:                                                  | The generation lock ID                                              |
| `secrets`                                                           | Dict[str, *str*]                                                    | :heavy_minus_sign:                                                  | A map of secrets to store in the GitHub target                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 4XX              | application/json |
| models.APIError  | 5XX              | \*/\*            |

## configure_code_samples

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

    res = test_sdk2.github.configure_code_samples(org="<value>", repo="<value>", target_name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `org`                                                               | *str*                                                               | :heavy_check_mark:                                                  | The GitHub organization name                                        |
| `repo`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The GitHub repository name                                          |
| `target_name`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The target name for the code samples                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GithubConfigureCodeSamplesResponse](../../models/githubconfigurecodesamplesresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 4XX              | application/json |
| models.APIError  | 5XX              | \*/\*            |

## configure_mintlify_repo

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

    test_sdk2.github.configure_mintlify_repo(org="<value>", repo="<value>", input_="<value>", overlays=[
        "<value>",
    ])

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `org`                                                               | *str*                                                               | :heavy_check_mark:                                                  | The GitHub organization name                                        |
| `repo`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The GitHub repository name                                          |
| `input`                                                             | *str*                                                               | :heavy_check_mark:                                                  | The input OpenAPI document                                          |
| `overlays`                                                          | List[*str*]                                                         | :heavy_check_mark:                                                  | The overlays to apply                                               |
| `subdirectory`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The subdirectory (location of mint.json)                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 4XX              | application/json |
| models.APIError  | 5XX              | \*/\*            |

## configure_target

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

    test_sdk2.github.configure_target(org="<value>", repo_name="<value>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `org`                                                               | *str*                                                               | :heavy_check_mark:                                                  | The GitHub organization name                                        |
| `repo_name`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The GitHub repository name                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 4XX              | application/json |
| models.APIError  | 5XX              | \*/\*            |

## trigger_action

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

    test_sdk2.github.trigger_action(org="<value>", repo_name="<value>", gen_lock_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `org`                                                               | *str*                                                               | :heavy_check_mark:                                                  | The GitHub organization name                                        |
| `repo_name`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The GitHub repository name                                          |
| `gen_lock_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The generation lock ID                                              |
| `target_name`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The target name for the action                                      |
| `set_version`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A version to override the SDK too in workflow dispatch              |
| `force`                                                             | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Force an SDK generation                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 4XX              | application/json |
| models.APIError  | 5XX              | \*/\*            |

## get_action

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

    res = test_sdk2.github.get_action(org="<value>", repo="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `org`                                                               | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `repo`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `target_name`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The targetName of the workflow target.                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GithubGetActionResponse](../../models/githubgetactionresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 4XX              | application/json |
| models.APIError  | 5XX              | \*/\*            |