In Python, we usually express data structures like this using classes, and type annotations for variables. However, Python's type system is less strict compared to TypeScript's, for example it doesn't natively support union types. So we can't enforce the variable to only admit "WEREWOLF" or "VILLAGER" other than through runtime checks. 

Given these considerations, your TypeScript code can be transcribed into Python as follows:

```python
from GameDefs import Character

class GameEndMsg:
    def __init__(self, winner: str):
        assert winner in {"WEREWOLF", "VILLAGER"}, "Invalid value for winner"
        self.winner = winner
```

Note that here we use Python's built-in assertions to enforce the restriction on the value of "winner". If the assertion fails, the program will stop with an AssertionError.