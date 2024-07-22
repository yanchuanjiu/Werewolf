In Python, you can achieve the same functionality by using the `update()` method on dictionaries.

Here is the equivalent Python code for your TypeScript function:

```python
def set_obj(old_obj, new_obj):
    old_obj.update(new_obj)
```

This will update `old_obj` with the key-value pairs from `new_obj`, overwriting existing keys in `old_obj`. 

In the original TypeScript code, the TypeScript type `T` is cast to `Record<string, any>` which is equivalent to a dictionary in Python. However, Python is dynamically typed, so we don't need to specify or cast the types.