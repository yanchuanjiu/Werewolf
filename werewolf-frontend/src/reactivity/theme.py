In Python, we have no direct analog for Vue's "computed" function, but we can mimic its behavior with property decorators. Here's how you might translate your TypeScript code:

```python
from .game import date

DARK = "-dark"
LIGHT = ""

class Theme:
    @property
    def theme(self):
        return DARK if date.value % 2 == 0 else LIGHT
```

Remember that Python does not support importing/exporting in the same way TypeScript does. By defining `theme` as a property of the `Theme` class, we are making it available for other parts of our application to access. They can create an instance of `Theme` class and access the `theme` property, which will compute its value dynamically based on condition just like the vue's "computed".