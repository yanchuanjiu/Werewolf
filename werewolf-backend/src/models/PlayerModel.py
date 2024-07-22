Here is the Python version of the TypeScript code you provided:

```python
import random
import time
from werewolf_frontend.shared.GameDefs import Character
from werewolf_frontend.shared.ModelDefs import (
    CharacterStatus, day, ID, index, PlayerDef, PublicPlayerDef)
from RoomModel import Room 

class Player():
    def __init__(self, name, index):
        self.character = None  # is set when game begins
        self.hasVotedAt = []
        self.sheriffVotes = []
        self.isAlive = True
        self.isSheriff = False
        self.die = None
        self.characterStatus = CharacterStatus()
        self.index = index
        self.name = name
        self._id = '{}.{}'.format(
            random.randint(1000, 9999),  # just for the same string length as in TS
            int(time.time() * 1000))  # to get the milliseconds
        self.isDying = False
        self.canBeVoted = False

    def getPublic(self, room):
        return PublicPlayerDef(
            self.index,
            self.isAlive,
            self.isSheriff,
            self.name,
            self == room.curDyingPlayer,
            self.hasVotedAt,
            self.sheriffVotes,
        )
```
The translation keeps the spirit of the original JavaScript code but takes some liberties as it's not possible to directly translate everything. Particularly note that:

- There's no access control in Python (e.g., public/protected properties in TypeScript), so all members are just normal members.

- Python doesn't support `interface`s like TypeScript does. Its philosophy is that "if it walks like a duck and talks like a duck, it's a duck", i.e. it emphasizes behaviors rather than formal interfaces. Thus, we can't implement an interface like `PlayerDef` directly. If necessary, we can create an abstract base class.

- Python does not have an equivalent to TypeScript's half-open intervals for random float numbers; I'm using randint for a similar output in terms of string length.

- Python has no optional chaining `?.`. It also does not have equivalent undefined types, which can be an issue as Python raises an exception when trying to access a non-existent dictionary key (unlike JavaScript, which returns undefined). Here, I've replaced the undefined by initializing with None.