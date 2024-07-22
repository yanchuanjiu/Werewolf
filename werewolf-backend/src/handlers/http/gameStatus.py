Python doesn't have an exact equivalent to TypeScript's import/export system and middleware pattern (commonly used in Node.js applications like Koa or Express). However, the above code could be written in Python using a web framework such as Flask.

Here is a closest translation:

```python
from flask import Flask, request, jsonify

IDHeaderName = "id-header-name" # import from the respective python file
RoomNumberHeaderName = "room-number-header-name" # import from the respective python file
Room = RoomModel # import from the respective python file
Player = PlayerModel # import from the respective python file

# define global variable with the game status
game_status = {}

app = Flask(__name__)

@app.route('/gameStatus', methods=['POST'])
def game_status():
    playerID = request.headers.get(IDHeaderName)
    roomNumber = request.headers.get(RoomNumberHeaderName)

    room = Room.get_room(roomNumber)
    curPlayer = room.get_player_by_id(playerID)

    ret = {
        "status": 200,
        "msg": "ok",
        "data": {
            "self": curPlayer,
            "curDay": room.currentDay,
            "gameStatus": room.curStatus,
            "players": room.players if room.isFinished else room.choosePublicInfo()
        }
    }

    return jsonify(ret)

if __name__ == '__main__':
    app.run(port=5000)
```

In this Python Flask application, `'/gameStatus'` endpoint is to mimic the `gameStatus` middleware function from the original TypeScript code. This code doesn't deal with async tasks as in your original TypeScript code, and error handling is also not included. You should add try-except blocks where needed. 

Please note: The code is assuming there are `get_room` and `get_player_by_id` methods implemented in `RoomModel` and `PlayerModel` classes respectively. It also assumes that `IDHeaderName` and `RoomNumberHeaderName` are defined somewhere else in your Python code, so it only provided placeholders.