In Python, we don't have the exact same libraries or techniques to represent reactivity like in Vue3, so I'll provide a simple translation that comes closest to achieving something similar in Python:

```python
from typing import List
from shared.GameDefs import Character, GameStatus, TIMEOUT
from shared.ModelDefs import CharacterStatus, Day, GameEvent, PlayerDef, PublicPlayerDef
from http.gameStatus import get_game_status

# 玩家的公开信息
players: List[PublicPlayerDef] = []
# 角色配置
needing_characters: List[Character] = []
# 自己的详细状态
self = PlayerDef("", "", [], 0, False, False, "---", [], False, False)
# 自己的角色
character = self.character if self else ""
# 天数
date: Day = -1
# 当前游戏进程
game_status: GameStatus = GameStatus.WOLF_KILL
# 当前状态还有多结束
game_status_time_left = TIMEOUT[GameStatus.WOLF_KILL]


# gameStatus 被修改时调用, 改变 ui 状态, 弹出提示等


# 获得最新的游戏信息
async def refresh():
    data = await get_game_status({})
    if not data:
        return

    date = data.cur_day
    game_status = data.game_status
    players = data.players
    self = data.self
```

This Python code snippet makes use of Python's typing module for static type checking similar to TypeScript. Also, unlike TypeScript, Python does not have support for reactivity (refs, computed, etc.) out of the box.

Note that, unlike in JavaScript and TypeScript, Python uses snake_case for variable names instead of camelCase. This is reflected in my translation.