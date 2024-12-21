# AccessToken

An AccessToken is a token that can be used to authenticate with the Speakeasy API.


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `access_token`                                               | *str*                                                        | :heavy_check_mark:                                           | N/A                                                          |
| `claims`                                                     | [models.Claims](../models/claims.md)                         | :heavy_check_mark:                                           | N/A                                                          |
| `user`                                                       | [models.AccessTokenUser](../models/accesstokenuser.md)       | :heavy_check_mark:                                           | N/A                                                          |
| `workspaces`                                                 | List[[models.WorkspacesModel](../models/workspacesmodel.md)] | :heavy_minus_sign:                                           | N/A                                                          |
| `feature_flags`                                              | List[[models.FeatureFlag](../models/featureflag.md)]         | :heavy_minus_sign:                                           | N/A                                                          |