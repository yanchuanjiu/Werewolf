Python does not have TypeScript’s static typing system, nor does it have built-in server-side events as io does. To simulate async behavior, I'll setup some classes to encapsulate room, player, event buses and messaging. Here's a rough translation of your code into Python:

```python
from .. import io
from werewolf_frontend.shared.WSEvents import Events
from werewolf_frontend.shared.WSMsg.GameEnd import GameEndMsg
from ...models.RoomModel import Room

CLEAR_ROOM_TIME = 3600

class Player:
    # define your Player class attributes and methods here
    pass

class checkGameOver:
    def __init__(self, room):
        self.room = room

    def count_alive_players(self):
        players = {'werewolf': 0, 'villager': 0}
        for p in self.room.players:
            if p.isAlive:
                if p.character == "WEREWOLF":
                    players['werewolf'] += 1
                else:
                    players['villager'] += 1
        return players

    def game_over(self):
        players = self.count_alive_players()
        werewolf = players['werewolf']
        villager = players['villager']
        if werewolf >= villager or werewolf == 0:
            winner = 'VILLAGER' if werewolf == 0 else 'WEREWOLF'
            io.to(self.room.roomNumber).emit(Events.GAME_END, {'winner': winner})
            self.room.isFinished = True
            self.room.timer.cancel()
            self.room.clearSelfTimer.cancel()
            io.socketsLeave(self.room.roomNumber)
            io.in_(self.room.roomNumber).disconnectSockets(True)
            Room.clearRoom(self.room.roomNumber, CLEAR_ROOM_TIME)
            return True
        else:
            return False
```
Please note that this is a rough translation and may require tweaking based on your exact use case. Python has different frameworks that can be used for networking applications (like Flask and Django). If you're using one of these, you'll need to adjust this code to follow the conventions of these frameworks.