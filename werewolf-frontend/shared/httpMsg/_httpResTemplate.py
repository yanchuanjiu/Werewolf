In Python, we generally use classes instead of interfaces. The TypeScript interface can be represented by creating a Python class as follows:

```python
class HttpRes:
    def __init__(self, status: int, msg: str, data):
        self.status = status
        self.msg = msg
        self.data = data
   ```
In the code above, HttpRes class holds three attributes - status, msg, and data. The data type of status and msg is integer and string respectively, just like the TypeScript code. The "data" attribute does not have a specific data type because in Python variables are dynamically typed. It is equivalent to using a generic '<T = {}>' type in TypeScript.