In Python, the concept of importing modules and using them is somewhat similar to TypeScript. However, Python doesn't have direct counterparts for TypeScript's specific features such as type annotation and import/export statements. Here's a close Python equivalent to your TypeScript code.

Assuming that `showDialog` and `ShowMsg` are defined somewhere in your Python modules.

```python
from path.to.your.module import ShowMsg, showDialog

def showWSMsg(msg: ShowMsg) -> None:
    showDialog(msg.innerHTML, msg.showTime)
```

Here:

1. `path.to.your.module` represents the file path to the module containing the `ShowMsg` and `showDialog` objects, which you need to replace with your actual path.
2. In Python, type hinting is optional. In your TypeScript function, you're specifying that `msg` is of type `ShowMsg`. In the equivalent Python function, `msg` is hinted to be of type `ShowMsg` and the return type is `None` (meaning the function doesn't return anything).
3. The use of `.` in `msg.innerHTML` and `msg.showTime` implies that `msg` is an object of a class that has `innerHTML` and `showTime` as attributes. If `ShowMsg` is a class, ensure it has these attributes.

Please replace `from path.to.your.module import ShowMsg, showDialog` with the actual path where `ShowMsg` and `showDialog` are defined in your Python script.