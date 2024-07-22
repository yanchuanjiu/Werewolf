Python doesn't have a direct equivalent for all TypeScript features and libraries. The closest Python equivalent for the given TypeScript code could be something like this:

```Python
from collections import namedtuple
from enum import Enum

ActionInfo = namedtuple("ActionInfo", ["content", "is_shown", "disabled", "no_target", "on_click"])

class Character(Enum):
    WEREWOLF = 1
    SEER = 2
    WITCH = 3
    GUARD = 4
    HUNTER = 5

class GameStatus(Enum):
    EXILE_VOTE = 1
    SHERIFF_VOTE = 2
    SHERIFF_ELECT = 3
    WOLF_KILL = 4
    SEER_CHECK = 5
    WITCH_ACT = 6
    GUARD_PROTECT = 7
    SHERIFF_ASSIGN = 8
    HUNTER_SHOOT = 9
    DAY_DISCUSS = 10
    SHERIFF_SPEECH = 11
    LEAVE_MSG = 12

game_status = GameStatus.EXILE_VOTE 
players = None
self = {'value': {'character': Character.WEREWOLF}}
potion = {'value': ''}
action_info_list = []

# This is a placeholder for the content of the action_info_list, replace it with the real values and methods
action_info_list = [
  ActionInfo('action name', lambda:True, lambda: game_status.value != GameStatus.EXILE_VOTE, False, None)
]
run_action_list = [info for info in action_info_list if info.is_shown]
```
In this code, I have used namedtuple to create the ActionInfo object representing an action item similar to the objects in the JavaScript array. I have used the enum package to define the GameStatus and Character enums. 

Please also notice that Vue.js specific code (import from 'vue' and usage of `h`, `vShow`, `withDirectives` and `ActionBtn.vue` (Vue component)) cannot be translated to Python directly as Vue.js is a frontend framework for JavaScript and there is no equivalent in Python. Thus, those parts are omitted. 

You need to adapt this code according to needs of your Python environment (web framework, GUI toolkit, game engine or other).