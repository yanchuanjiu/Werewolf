Here is the Python equivalent code for your TypeScript:

```python
from .. import io
from werewolf_frontend.shared.constants import IDHeaderName, RoomNumberHeaderName
from werewolf_frontend.shared.GameDefs import GameStatus
from werewolf_frontend.shared.httpMsg._httpResTemplate import HttpRes
from werewolf_frontend.shared.httpMsg.CharacterAct import CharacterAct
from werewolf_frontend.shared.WSEvents import Events
from middleware.handleError import create_error
from models.PlayerModel import Player
from models.RoomModel import Room
from gameActHandlers import status2_handler
from gameActHandlers.validateIdentity import validate_identity

# handle game begin
async def game_begin(ctx):
    room_number = ctx.get(RoomNumberHeaderName)
    player_id = ctx.get(IDHeaderName)

    room = Room.get_room(room_number)
    if room.creator_id != player_id:
        create_error({'msg': "只有房主才能开始游戏", 'status': 401})

    if len(room.players) != len(room.needing_characters):
        create_error({'msg': "房间人数未满, 无法开始游戏", 'status': 401})

    # assign characters
    needing_characters = list(room.needing_characters)

    for p in room.players:
        index = random.randint(0, len(needing_characters) - 1)
        character = needing_characters.pop(index)

        p.character = character
        if character == "GUARD":
            p.character_status = {'protects': []}
        elif character == "HUNTER":
            p.character_status = {'shootAt': {'day': -1, 'player': -1}}
        elif character == "SEER":
            p.character_status = {'checks': []}
        elif character == "WEREWOLF":
            p.character_status = {'wantToKills': []}
        elif character == "WITCH":
            p.character_status = {'POISON': {'usedDay': -1, 'usedAt': -1},
                                  'MEDICINE': {'usedDay': -1, 'usedAt': -1}}
        elif character == "VILLAGER":
            p.character_status = {}
        else:
            pass

    io.to(room_number).emit(Events.GAME_BEGIN)
    status2_handler[GameStatus.WOLF_KILL].start_of_state(room, False)

    ctx.body = {'data': {}, 'msg': "ok", 'status': 200}
```