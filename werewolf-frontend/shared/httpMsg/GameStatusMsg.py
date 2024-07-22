Python doesn't have a direct equivalent to TypeScript's static types and interfaces, but for documenting and providing limited type checking functionality, Python has type hints which are available from Python 3.5 and later. Also, Python has a built-in library named `dataclasses` introduced in Python 3.7 which works quite similarly to TypeScript's `interface`.

However, the import statements wouldn't be necessary in Python since there aren't any such packages or files provided. If they exist, you may import them like any other Python libraries. Also, Python doesn't have `PublicPlayerDef[]` like syntax. We use `list` method for the same.

Here is your translated code with Python's type hints and dataclasses:

```python
from typing import List
from dataclasses import dataclass

@dataclass
class GameStatusRequest:
    pass

@dataclass
class GameStatusResponse:
    players: List[PublicPlayerDef]
    self: PlayerDef
    curDay: day
    gameStatus: GameStatus
```

Remember, Python type hints are just hints and won't enforce type checking like TypeScript. They are largely helpful for readability and tooling.