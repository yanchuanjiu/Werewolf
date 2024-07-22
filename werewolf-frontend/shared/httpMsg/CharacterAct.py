In Python, there's no direct equivalent of TypeScript's interfaces as Python is a dynamically-typed language. But you can achieve similar functionality using data classes (in Python 3.7+) or NamedTuple (in Python 3.5+). Both of these can be used to create classes which are used to store value and do not have methods.

Given the information providing from the TypeScript, you may just want to create a simple class in Python. Here is the equivalent code.

```python
from ModelDefs import index  # Assuming "index" is a class in module "ModelDefs".

class CharacterAct:
    def __init__(self, target: index):
        """
        The target player's index number for the operation.
        If it is a witch, the positive number represents saving people, and the negative number represents killing.
        """
        self.target = target
```

If `index` just refers to integer indexing:

```python
class CharacterAct:
    def __init__(self, target: int):
        """
        The target player's index number for the operation.
        If it is a witch, the positive number represents saving people, and the negative number represents killing.
        """
        self.target = target
```