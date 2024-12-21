# GithubConfigureMintlifyRepoRequest

A request to configure a GitHub repository for mintlify


## Fields

| Field                                    | Type                                     | Required                                 | Description                              |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `org`                                    | *str*                                    | :heavy_check_mark:                       | The GitHub organization name             |
| `repo`                                   | *str*                                    | :heavy_check_mark:                       | The GitHub repository name               |
| `input`                                  | *str*                                    | :heavy_check_mark:                       | The input OpenAPI document               |
| `overlays`                               | List[*str*]                              | :heavy_check_mark:                       | The overlays to apply                    |
| `subdirectory`                           | *Optional[str]*                          | :heavy_minus_sign:                       | The subdirectory (location of mint.json) |