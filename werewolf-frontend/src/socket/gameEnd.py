Python doesn't have import syntax like TypeScript, but you can achieve the same functionality using different OOP design principles such as composition and inheritance. The overall structure of your code would change significantly.

Python also doesn't have async/await like TypeScript does natively. We can use Python's asyncio library to achieve asynchronous functionality. Here's a rough translation/implementation of your TypeScript code:

```python
from ModelDefs import PlayerDef
from WSMsg.GameEnd import GameEndMsg
from computeGameEvents import groupedGameEvents
from dialog import showDialog
from game import players, refresh, self
from joinRoom import roomNumber
from record import saveRecord
from router import router
from socket import socket

class GameEnd:
    def __init__(self, socket, refresh, saveRecord, showDialog, router):
        self.socket = socket
        self.refresh = refresh
        self.saveRecord = saveRecord
        self.showDialog = showDialog
        self.router = router

    async def game_end(self, msg: GameEndMsg):
        self.socket.removeAllListeners()
        self.socket.disconnect()

        await self.refresh()

        time = datetime.datetime.now()

        self.saveRecord(
            groupedGameEvents.value,
            roomNumber.value,
            self.value,
            [player for player in players.value],
            time
        )

        self.showDialog(
            f"<b>游戏结束</b> </br> 获胜者为{'狼人' if msg.winner == 'WEREWOLF' else '村民'}"
        )

        self.router.replace({
            "name": "review-detail",
            "query": {
                "roomNumber": roomNumber.value,
                "time": time,
            },
        })
```
In the Python version, we are creating a class GameEnd with methods taking in necessary dependencies/utilities/functions as parameters in the constructor. This emulates the import actions that TypeScript does. 

Note: Python does not have type checking like TypeScript. The `msg: GameEndMsg` inside the `game_end` method is a hint to the developer but Python will not enforce it.