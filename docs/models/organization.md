# Organization

A speakeasy organization


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `name`                                                               | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `slug`                                                               | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `account_type`                                                       | [models.AccountType](../models/accounttype.md)                       | :heavy_check_mark:                                                   | N/A                                                                  |
| `telemetry_disabled`                                                 | *bool*                                                               | :heavy_check_mark:                                                   | N/A                                                                  |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `updated_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `sso_activated`                                                      | *bool*                                                               | :heavy_check_mark:                                                   | N/A                                                                  |
| `free_trial_expiry`                                                  | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `sso_connection_id`                                                  | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | N/A                                                                  |
| `internal`                                                           | *Optional[bool]*                                                     | :heavy_minus_sign:                                                   | N/A                                                                  |