The TypeScript code you're asking for conversion makes use of some JavaScript-specific features like modules, asynchronous functions, and particular libraries (koa). However, here is an attempt to provide a comparable implementation to the code provided in Python:

Note: Due to Python and Javascript language differences, not all features and functionality can be directly translated.

```python
from thriftpy.server import socket
from ...werewolf_frontend.shared.GameDefs import GameStatus, TIMEOUT
from ...werewolf_frontend.shared.ModelDefs import index
from ...werewolf_frontend.shared.WSEvents import Events
from ...werewolf_frontend.shared.WSMsg.ChangeStatus import ChangeStatusMsg
from ..models.PlayerModel import Player
from ..models.RoomModel import Room
from .ExileVote import ExileVoteHandler
from . import startCurrentState
import threading

class DayDiscussHandler:
    curStatus = GameStatus.DAY_DISCUSS

    @staticmethod
    async def handle_http_in_the_state(room, player, target, ctx):

        room.to_finish_players.delete(player.index)

        if len(room.to_finish_players) == 0:
            threading.Timer(0, room.timer).cancel()
            DayDiscussHandler.end_of_state(room)

        return {
            "status": 200,
            "msg": "ok",
            "data": {"target": target}
        }
    
    @staticmethod
    def start_of_state(room):
        startCurrentState(DayDiscussHandler, room)

    @staticmethod
    async def end_of_state(room):
        room.next_state_of_die_check = GameStatus.WOLF_KILL
        await ExileVoteHandler.start_of_state(room)
```

This translation assumes that you have a similar asynchronous structure in place for Python (i.e., your Python framework supports async/await). Different packages/modules names are used to reflect usual Python project structure. Adjust as per your actual project requirements.