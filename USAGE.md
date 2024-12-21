<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import os
import test_sdk_package
from test_sdk_package import TestSdk2

with TestSdk2(
    security=test_sdk_package.Security(
        api_key=os.getenv("TESTSDK2_API_KEY", ""),
    ),
) as test_sdk2:

    res = test_sdk2.generate_code_sample_preview(languages=[
        "<value>",
        "<value>",
    ], schema_file={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    })

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import os
import test_sdk_package
from test_sdk_package import TestSdk2

async def main():
    async with TestSdk2(
        security=test_sdk_package.Security(
            api_key=os.getenv("TESTSDK2_API_KEY", ""),
        ),
    ) as test_sdk2:

        res = await test_sdk2.generate_code_sample_preview_async(languages=[
            "<value>",
            "<value>",
        ], schema_file={
            "file_name": "example.file",
            "content": open("example.file", "rb"),
        })

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->