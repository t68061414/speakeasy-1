# SuggestOpenAPIRegistryRequest


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `x_session_id`                                                         | *str*                                                                  | :heavy_check_mark:                                                     | N/A                                                                    |
| `namespace_name`                                                       | *str*                                                                  | :heavy_check_mark:                                                     | N/A                                                                    |
| `revision_reference`                                                   | *str*                                                                  | :heavy_check_mark:                                                     | Tag or digest                                                          |
| `suggest_request_body`                                                 | [Optional[models.SuggestRequestBody]](../models/suggestrequestbody.md) | :heavy_minus_sign:                                                     | Suggest options                                                        |