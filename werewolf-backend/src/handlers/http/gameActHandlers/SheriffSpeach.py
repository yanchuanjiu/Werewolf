Python doesn't have direct equivalents for TypeScript's classlike structure, module system, and static typing. Because of this, the following Python code simplifies some of the class and module structures, and leaves out the type declarations:

```python
# The import paths would need to be replaced with relative Python import paths

from .. import io 
from .......werewolf_frontend.shared import GameDefs
from .......werewolf_frontend.shared import ModelDefs
from .......werewolf_frontend.shared import WSEvents
from .......werewolf_frontend.shared.WSMsg import ChangeStatus
from ..middleware import handleError
from ..models import PlayerModel
from ..models import RoomModel
from ..utils import get_vote_result
from . import GameActHandler, Response, start_current_state
from .SheriffVote import SheriffVoteHandler

class SheriffSpeachHandler(GameActHandler):
    cur_status = GameDefs.GameStatus.SHERIFF_SPEECH

    @staticmethod
    async def handle_http_in_the_state(room, player, target, ctx):
        # 结束自己的发言
        room.to_finish_players.discard(player.index)

        # 如果所有人都发言完毕, 进入警长投票环节
        if len(room.to_finish_players) == 0:
            await SheriffVoteHandler.start_of_state(room)

        return {
          'status': 200,
          'msg': "ok",
          'data': {'target': target},
        }

    @staticmethod
    async def start_of_state(room):
        start_current_state(SheriffSpeachHandler, room)

    @staticmethod
    async def end_of_state(room):
        await SheriffVoteHandler.start_of_state(room)
```

// TODO 在24h后删除房间

Please replace the import paths with correct relative paths in your Python project. Python's async coroutine functionality, used in the async and await keywords in the TypeScript, is preserved here, but you'll need an appropriate Python ASGI server to run it.