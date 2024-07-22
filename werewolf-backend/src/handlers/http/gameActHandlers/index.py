Python does not have TypeScript's exact type checking feature or its exact module import styles, so the code will apply Python's classes, methods, and import styles instead. Here is a translation reflecting key elements of the original code:

In Python, we define interfaces as classes; all methods are abstract and need to be implemented by any class that uses this as a base.

```python
from abc import ABC, abstractmethod

class Response(ABC):
    def __init__(self, status, msg, data):
        self.status = status
        self.msg = msg
        self.data = data

class GameActHandler(ABC):
    
    @abstractmethod
    def handleHttpInTheState(self, room, player, target, ctx): pass

    @abstractmethod
    def startOfState(self, room, *rest): pass

    @abstractmethod
    def endOfState(self, room, *rest): pass

    @abstractmethod
    def curStatus(self): pass
```

Following this, we can write Python versions of the functions `startCurrentState` and `gotoNextStateAfterHandleDie`, along with the dictionary that maps game statuses to their corresponding handlers.

```python
from shared.GameDefs import GameStatus, TIMEOUT
from shared.WSEvents import Events
from shared.WSMsg.ChangeStatus import ChangeStatusMsg
from models.PlayerModel import Player
from models.RoomModel import Room
from utils.checkGameOver import checkGameOver

# Implement the status2Handler dictionary after importing all handler classes.
status2Handler = {
  GameStatus.DAY_DISCUSS: DayDiscussHandler,
  # More game statuses and handlers go here...
}

def startCurrentState(handler, room, *extra):
    if room.curStatus != handler.curStatus:
        room.gameStatus.append(handler.curStatus)

    timeout = TIMEOUT[handler.curStatus]
    room.timer = time.time() + timeout
    handler.endOfState(room, *extra)
    
    io.to(room.roomNumber).emit(Events.CHANGE_STATUS, {
        'setDay': room.currentDay,
        'setStatus': handler.curStatus,
        'timeout': timeout
    } as ChangeStatusMsg)

def gotoNextStateAfterHandleDie(room):
    if checkGameOver(room): return
    room.curDyingPlayer.isDying = False
    room.curDyingPlayer.isAlive = False
    dyingPlayer = next((p for p in room.players if p.isDying), None)
    
    if dyingPlayer:
        room.curDyingPlayer = dyingPlayer
        LeaveMsgHandler.startOfState(room)
    else:
        room.curDyingPlayer = None
        if room.nextStateOfDieCheck == GameStatus.DAY_DISCUSS:
            room.toFinishPlayers = set(p.index for p in room.players if p.isAlive)
            for p in room.players: 
                p.canBeVoted = p.isAlive
        status2Handler[room.nextStateOfDieCheck].startOfState(room)
        room.nextStateOfDieCheck = None
```

Note that there are some placeholder import statements, and the logic of the game, some concepts, definitions and even some methods may need to be modified to be viable in Python.