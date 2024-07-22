Python, being a dynamically typed language, does not have an exact equivalent to TypeScript's interfaces and types. However, the fact that TypeScript is statically typed and Python is dynamically typed cannot be exactly translated. 

However, to give you an equivalent, you can use Python data classes to represent the data structures you have in TypeScript. Here's how you might implement the TypeScript code you've given in Python:

```python
from dataclasses import dataclass, field
from typing import List, Optional
from ../GameDefs import Character
from ../ModelDefs import ID, index
from ./_httpResTemplate import HttpRes

@dataclass
class CreateRoomRequest:
    characters: List[Character]
    password: Optional[str] = field(default=None)
    name: str

@dataclass
class CreateRoomResponse(HttpRes):
    room_number: str
    ID: ID
```

Note: The HttpResTemplate is not a valid python implementation, you need to change it according to Python code.