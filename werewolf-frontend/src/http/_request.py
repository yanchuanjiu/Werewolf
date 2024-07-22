Python doesn't have a built-in equivalent to TypeScript's Axios, but you can use the requests library, which is a popular HTTP request library in Python. Here is a translation of your function to Python

Python doesn't directly import constants from other modules like TypeScript, you just import the module and then use the constants as attributes of the module. Here is the translated code:

```python
import requests
import shared.constants as constants
import shared.httpMsg._httpResTemplate as httpResTemplate
import reactivity.dialog as dialog
import utils.token as token

def request(config):
    with requests.Session() as session:
        session.base_url = constants.SERVER_BASE_URL
        session.timeout = 60
        session.headers.update({'withCredentials': 'true'})

    try:
        token = token.getToken()
        if token:
            config['headers'][constants.IDHeaderName] = token.ID
            config['headers'][constants.RoomNumberHeaderName] = token.roomNumber

        response = session.get(config[0], params=config[1])

        if response.status_code == 200:
            return response.json()
        else:
            data = response.json()
            if 'msg' in data:
                dialog.showDialog(data['msg'])
            else:
                print("# e", response)
                dialog.showDialog("Don't know what happened QwQ")
                
    except Exception as err:
        print(err)
```

Notes:
- Python's requests library does not have the concept of interceptors, so you may need to rewrite your axios interceptors in another way.
- Python has no counterpart of TypeScript's concept of type, so HttpRes is omitted.
- Python's asynchronous and Typescript's asynchronous are not the same. Python's are concurrent using coroutines, not Promise-based. We use the normal execution for Python in this case.
- Error handling in Python is typically done with try-except blocks.
- `(res as unknown) as HttpRes<T>`) has no direct equivalent in Python and is omitted.
- JavaScript's camelCase convention is converted to Python's snake_case convention.
- Python does not have the ternary operator like `&&` for None-able types, you may want to use explicit `if` checks.
- Python uses `None` instead of `null`.