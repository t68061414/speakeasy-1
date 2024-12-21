# Namespace

A namespace contains many revisions.


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `id`                                                                         | *str*                                                                        | :heavy_check_mark:                                                           | {organization_slug}/{workspace_slug}/{namespace_name}                        |
| `name`                                                                       | *str*                                                                        | :heavy_check_mark:                                                           | A human-readable name for the namespace.                                     |
| `created_at`                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects)         | :heavy_check_mark:                                                           | N/A                                                                          |
| `updated_at`                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects)         | :heavy_check_mark:                                                           | N/A                                                                          |
| `public`                                                                     | *Optional[bool]*                                                             | :heavy_minus_sign:                                                           | Indicates whether the namespace is publicly accessible                       |
| `composite_spec_metadata`                                                    | [Optional[models.CompositeSpecMetadata]](../models/compositespecmetadata.md) | :heavy_minus_sign:                                                           | N/A                                                                          |