In Python, since there is no concept of interfaces, we can represent the same using classes. Instead of importing interfaces in TypeScript, you import modules in Python:

```python

class ChangeStatusMsg:
    def __init__(self, set_day: 'day', set_status: 'GameStatus', timeout: int):
        self.set_day = set_day
        self.set_status = set_status
        self.timeout = timeout
```

In the above Python code, `'day'` and `'GameStatus'` are expected to be defined somewhere else in your codebase, as a class or any other data types. The comments in TypeScript code have been removed as in Python you would generally define these details in a docstring.