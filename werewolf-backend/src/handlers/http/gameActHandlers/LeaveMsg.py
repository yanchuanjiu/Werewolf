In Python, I would implement similar functionality using classes due to Python's object-oriented nature. Here is how I would translate the TypeScript code to Python:

```python
from werewolf_frontend.shared import GameDefs, ModelDefs, WSEvents, WSMsg
from models import PlayerModel, RoomModel
from utils import get_vote_result
import current_state, hunter_shoot


class LeaveMsgHandler:
    cur_status = GameDefs.GameStatus.LEAVE_MSG

    @staticmethod
    def handleHttpInTheState(room: RoomModel.Room, player: PlayerModel.Player, 
                             target: ModelDefs.index, ctx) -> dict:
        LeaveMsgHandler.endOfState(room)
        return {
            "status": 200,
            "msg": "ok",
            "data": {"target": target}
        }

    @staticmethod
    def startOfState(room: RoomModel.Room):
        if not room.next_state_of_die_check:
            raise Exception("未设置死亡结算后去到的状态")
        if room.current_day == 1 or room.next_state_of_die_check == GameDefs.GameStatus.WOLF_KILL:
            current_state.startCurrentState(room)
        else:
            LeaveMsgHandler.endOfState(room)

    @staticmethod
    def endOfState(room: RoomModel.Room):
        hunter_shoot.HunterShootHandler.startOfState(room)
```

Please note that you need to replace the detailed imports at the first line with your own module names. The Python version of the code is given assuming the module structure to be similar to the TypeScript version. 

Python doesn't have default exports as TypeScript, so it direct access was used. If such classes don't exist, you may need to create them in the respective modules/files. Also, remember that Python does not natively support an equivalent to the JavaScript context (`ctx`), so would need to replicate that functionality some other way if it's required in your Python environment.