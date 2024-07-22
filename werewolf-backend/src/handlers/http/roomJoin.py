In Python we do not have the concept of importing individual functions or variables directly like TypeScript. However, we can import the whole module or create an alias. Also, there are not tight data types as in TypeScript in Python. Here how it can be translated playing with the names:

```python
from werewolf_frontend.shared import GameDefs
from werewolf_frontend.shared.httpMsg import JoinRoomMsg
from werewolf_frontend.shared.WSEvents import Events
from werewolf_frontend.shared.WSMsg import RoomJoin
from models import PlayerModel as Player, RoomModel as Room
from gameActHandlers import status2Handler

from index import io

async def room_join(ctx):
  req = ctx.request.body

  name = req['name']
  password = req['password']
  room_number = req['roomNumber']

  room = Room.getRoom(room_number)

  player = room.playerJoin(name, password)

  ret = {
    'status': 200,
    'msg': 'ok',
    'data': {
      'ID': player._id,
      'index': player.index,
      'needingCharacters': room.needingCharacters,
    },
  }

  room_join_msg = room.choosePublicInfo()

  io.to(room_number).emit(Events.ROOM_JOIN, room_join_msg)

  ctx.body = ret
```
This translation will be accurate if similar classes and methods are implemented in Python. Please adjust as per your application design in Python.