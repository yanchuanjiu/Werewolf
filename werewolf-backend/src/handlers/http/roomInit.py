Python's Flask could be used as an equivalent to Koa, which is a web framework in Node.js. Here's the equivalent code in Python:

```python
from flask import Flask, request, jsonify
from werewolf_frontend.shared.constants import RoomNumberHeaderName
from werewolf_frontend.shared.httpMsg.InitRoomMsg import InitRoomRequest, InitRoomResponse
from models.RoomModel import Room

app = Flask(__name__)

@app.route('/roomInit', methods=['GET'])
def room_init():
    room_number = request.headers.get(RoomNumberHeaderName)
    room = Room.get_room(room_number)

    ret = InitRoomResponse(
        status=200,
        msg="ok",
        data={
            'players': room.choose_public_info(),
            'needingCharacters': room.needing_characters
        }
    )

    return jsonify(ret.serialize())
```
In Python, the equivalent to TypeScript interfaces could be classes. Also, it's assumed that you have a method `.serialize()` in your `InitRoomResponse` class that turns class attributes into a dictionary, so you can convert it into JSON using `jsonify()`.