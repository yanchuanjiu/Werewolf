In Python, we don't have the concept of middleware in the same way as in Node JS or TypeScript. We also don't have a direct equivalent for type casting (as CreateRoomRequest) since Python is dynamically typed.

That said, if you want to achieve similar functionality with a Python web framework like Flask, here's how you might go about it.

Assuming that the CreateRoomMsg, PlayerModel and RoomModel modules have already been converted to Python:

```python
from werewolf_frontend.shared.httpMsg.CreateRoomMsg import CreateRoomRequest, CreateRoomResponse
from models.PlayerModel import Player
from models.RoomModel import Room
from flask import request, jsonify

def room_create():
    req = CreateRoomRequest(**request.get_json())
    characters = req['characters']
    name = req['name']
    password = req['password']

    creator = Player(index=1, name=name)

    room = Room(creator=creator, needingCharacters=characters, password=password)

    ret = CreateRoomResponse(status=200, msg='ok', data={
        'roomNumber': room.roomNumber,
        'ID': creator._id
    })

    return jsonify(ret)

```

Some assumptions have been made here:
1. In TypeScript, the fields of request are accessed as properties. In Python, they are accessed like dictionary keys. This code is assuming CreateRoomRequest is a dictionary-like object.
2. Flask's request.get_json() is used to parse JSON input similar to Koa's `ctx.request.body`.
3. The Player and Room constructor calls are assuming those classes take a set of keyword arguments, similar to JavaScript/TypeScript object syntax.