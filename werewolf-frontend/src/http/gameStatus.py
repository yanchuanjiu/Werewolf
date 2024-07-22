Python doesn't have a direct equivalent for TypeScript import system. This is normally handled by different modules in Python. In this case, you may use the `requests` module in Python to handle the HTTP requests. Here's how you can do the conversion:

```python
import requests
import json
from typing import Union

def get_game_status(data: dict) -> Union[dict, None]:
    res = requests.post("/game/status", data = data)

    if res.status_code != 200:
        return None

    return res.json()
```
In the Python code, I used Python's `requests` library which is similar to the idea of the `request` function being imported in your TypeScript code. One important note is that types for variables in Python is not as strict as TypeScript. In Python, you don't define the type of the data being passed or returned in the function parameters, but it is a good practice to denote the expected type using type hints as shown in this code snippet.

In TypeScript, `GameStatusRequest` and `GameStatusResponse` would be replaced by `dict` in Python, considering they are interfaces for simple JSON objects.