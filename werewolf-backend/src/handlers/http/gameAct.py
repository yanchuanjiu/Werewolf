Python doesn't have TypeScript's static typing, and some of the concepts used in TypeScript (like the Middleware interface and const keyword) are not directly translatable to Python. However, here is an equivalent Python script using Flask as the Python web framework:

```python
from flask import Flask, request

from shared.constants import IDHeaderName, RoomNumberHeaderName 
from shared.httpMsg import CharacterAct
from middleware.handleError import createError
from models.PlayerModel import Player
from models.RoomModel import Room
from gameActHandlers import status2Handler
from gameActHandlers.validateIdentity import validateIdentity

app = Flask(__name__)

@app.route('/gameAct', methods=['POST'])
def gameAct():
    req = request.get_json()
    
    roomNumber = request.headers.get(RoomNumberHeaderName)
    playerID = request.headers.get(IDHeaderName)
    
    room = Room.getRoom(roomNumber)
    player = room.getPlayerById(playerID)
    
    isValidate = validateIdentity(room, player)
    if isValidate != True:
        return createError({'status': 401, 'msg': isValidate})

    gameStatus = room.curStatus
    # TODO check character
    # TODO validate request
    
    # print("# gameAct", { 'gameStatus': gameStatus })
    
    # strategy pattern
    handler = None
    if gameStatus in status2Handler:
        handlerClass = status2Handler[gameStatus]
        if hasattr(handlerClass, 'handleHttpInTheState'):
            handler = handlerClass.handleHttpInTheState
    if handler:
        return handler(room, player, req['target'])
    else:
        return ''
```

This Python script implements similar functionalities to your TypeScript code, but keep in mind that Node.js (Javascript) and Python frameworks handle requests and responses differently. For example, ctx.body in Koa (Node.js) is similar to return 'Response' in Flask (Python).