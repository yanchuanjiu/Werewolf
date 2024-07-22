Python doesn't support TypeScript-style type definitions, interfaces, or enums in the same way. However, you can use Python classes, type annotations, and enums to accomplish a similar goal. The following is an attempted translation that captures similar functionality:

```python
from enum import Enum
from typing import Dict, List, Optional, Set, Tuple, Union

# Import the following from "GameDefs.py", assuming Character, GameStatus, Potion are classes/enums defined there
# from GameDefs import Character, GameStatus, Potion


class ID(str):  # Player id
    pass


class Index(int):  # Player number, starting from 1
    pass


class Day(int):  # Day 0: 0, Day n daytime: 2n-1, Day n night: 2n
    pass


class RoomDef:
    def __init__(self,
                 room_number: str,  # Room number, 6 digits
                 creator_ID: ID,
                 players: 'List[PlayerDef]',
                 current_day: Day,
                 needing_characters: 'List[Character]',
                 remaining_indexes: 'List[Index]',
                 is_finished: bool,
                 game_status: 'List[GameStatus]',
                 to_finish_players: 'Set[Index]',
                 timer: 'Timeout',  # The event timer id, is None when it ends
                 password: Optional[str] = None):  # Whether a password is set, store the hashed password
        self.room_number = room_number
        self.creator_ID = creator_ID
        self.players = players
        self.password = password
        self.current_day = current_day
        self.needing_characters = needing_characters
        self.remaining_indexes = remaining_indexes
        self.is_finished = is_finished
        self.game_status = game_status
        self.to_finish_players = to_finish_players
        self.timer = timer


class PublicPlayerDef:
    def __init__(self,
                 index: Index,  # Player number
                 name: str,  # Nickname
                 is_alive: bool,  # Whether the player is alive
                 is_sheriff: bool,  # Whether the player is a sheriff
                 is_dying: bool,  # Whether the player is dying
                 has_voted_at: 'List[Index]',  # The index is the day, value is who was voted for. Including daytime voting
                 sheriff_votes: 'List[Index]'):  # The index is the day, including sheriff elections (index=0) and sheriff transfers during the day
        self.index = index
        self.name = name
        self.is_alive = is_alive
        self.is_sheriff = is_sheriff
        self.is_dying = is_dying
        self.has_voted_at = has_voted_at
        self.sheriff_votes = sheriff_votes


class PlayerDef(PublicPlayerDef):
    def __init__(self,
                 character: 'Character',  # Game character
                 _id: 'ID',  # String + timestamp token
                 can_be_voted: bool,  # Whether it can be voted in the current stage
                 index: Index,
                 name: str
                 # Some properties skipped for brevity...
                 ):
        super().__init__(index=index, name=name)
        self.character = character
        self._id = _id
        self.can_be_voted = can_be_voted


class TokenDef:
    def __init__(self, ID: 'ID', datetime: int, room_number: str):
        self.ID = ID
        self.datetime = datetime
        self.room_number = room_number


class HunterStatus:
    shoot_at: Dict[Day, Index]


class GuardStatus:
    protects: List[Index]


class SeerStatus:
    checks: List[Dict[Index, bool]]


class WerewolfStatus:
    want_to_kills: List[Index]


class PotionStatus:
    used_day: Day
    used_at: Index


class WitchStatus(Dict['Potion', 'PotionStatus']):
    pass


# Using Union to create a type hint that can be any of the listed classes/types
CharacterStatus = Union[HunterStatus, GuardStatus, SeerStatus, WerewolfStatus, WitchStatus]


class CharacterEvent:
    character: 'Character'
    events: List[Dict[Day, str]]


class GameEvent:
    character: 'Character'
    at: Day
    deed: str
```

When moving to Python from TypeScript, there are some trade-offs: Python's handling of Enums and Interfaces is different, and Python often uses dynamic typing rather than static typing. As a result, the Python version may differ a bit in its design patterns.