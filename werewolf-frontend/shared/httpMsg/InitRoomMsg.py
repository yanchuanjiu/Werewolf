In Python, we typically do not have the concept of interfaces or types like in TypeScript. Here's a version of your code, but please note that Python won't force the shape of your objects to fit a particular schema like TypeScript does. However, Python includes the concept of classes, so we can use them to represent the structure implied by the TypeScript interfaces and types.

```python
from GameDefs import Character
from ModelDefs import PublicPlayerDef
from _httpResTemplate import HttpRes

class InitRoomRequest:
    pass

class InitRoomResponse(HttpRes):
    def __init__(self, players, needingCharacters):
        # Assuming HttpRes constructor takes a data parameter
        super().__init__({
            'players': players,
            'needingCharacters': needingCharacters,
        })

    @property
    def players(self):
        return self.data['players']

    @property
    def needingCharacters(self):
        return self.data['needingCharacters']
```

In Python, we typically use dynamic typing means checking whether an object has certain properties or methods at runtime. So we often don't do these kind of definitions. Python is more about making things work with duck typing rules - "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck."