# OrganizationUsage


## Fields

| Field                                                     | Type                                                      | Required                                                  | Description                                               |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `number_of_operations`                                    | *int*                                                     | :heavy_check_mark:                                        | Number of operations performed                            |
| `max_operations`                                          | *int*                                                     | :heavy_check_mark:                                        | Maximum Number of operations per SDK specific in contract |
| `language`                                                | *str*                                                     | :heavy_check_mark:                                        | The programming language used                             |
| `used_features`                                           | List[*str*]                                               | :heavy_check_mark:                                        | Features that have been used                              |
| `accessible_features`                                     | List[*str*]                                               | :heavy_check_mark:                                        | Features that are accessible                              |
| `accessible`                                              | *bool*                                                    | :heavy_check_mark:                                        | Indicates if the features are accessible                  |
| `workspaces`                                              | List[*str*]                                               | :heavy_check_mark:                                        | List of workspace IDs                                     |
| `gen_lock_ids`                                            | List[*str*]                                               | :heavy_check_mark:                                        | List of generation lock IDs                               |