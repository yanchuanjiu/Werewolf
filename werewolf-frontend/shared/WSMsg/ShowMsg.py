In Python, there are no interfaces. The closest equivalent are standard classes. However, Python doesn't have built-in support for optional properties like TypeScript. To handle optional values, we just use a default value (usually None). Here is a rough translation:

```python
from typing import Optional

class ShowMsg:
    def __init__(self, innerHTML: str, showTime: Optional[int]=None):
        self.innerHTML = innerHTML
        self.showTime = showTime
```
In this Python class, `innerHTML` is a required parameter and `showTime` is optional. 

The comments translated would be:
```python
from typing import Optional

class ShowMsg:
    """
    innerHTML: The message to display in the pop-up window.
    showTime: The display time(s), optional.
    """
    def __init__(self, innerHTML: str, showTime: Optional[int]=None):
        self.innerHTML = innerHTML
        self.showTime = showTime
```

However, remember that although type hinting gives hints for the developers and makes the code more robust and comprehensible, Python is dynamically-typed language and doesn't enforce these type checks at run time.