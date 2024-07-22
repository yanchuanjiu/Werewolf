In Python, there are no types so the type declarations in the TypeScript code will be removed. Also, Python doesn't support importing from a path as it is not a browser-based environment. 

However, it does support importing Python files (modules) in the same directory, or you can use various methods to import files in other directories. Furthermore, middleware doesn't exist in Python, so your application may need to use a web framework like Flask or Django for handling HTTP requests and responses.

Here's how you can implement the general logic of your provided TypeScript code in Python:

```python
from flask import Flask, request, abort, jsonify

app = Flask(__name__)

@app.route('/witchGetDie', methods=['GET'])
def witch_get_die():
    room_number = request.headers.get('RoomNumberHeaderName')
    player_id = request.headers.get('IDHeaderName')
    
    room = Room.get_room(room_number)
    player = room.get_player_by_id(player_id)
    
    if player.character != "WITCH":
        abort(401, "你的身份无法查看此消息")
    if player.character_status['MEDICINE']['used_at'] > 0:
        abort(401, "你已经用过解药, 无法查看死者")
    
    killed_by_wolf_today = ""
    for p in room.players:
        if p.die['from_character'] == "WEREWOLF" and p.die['at'] == room.current_day:
            killed_by_wolf_today = p.index
    
    ret = {"status": 200, "msg": "ok", "data": ""}
    if not killed_by_wolf_today:
        ret['data'] = "今晚无人被杀害"
    else:
        ret['data'] = "今晚被杀害的是:" + str(killed_by_wolf_today)
    
    return jsonify(ret), 200
```

Please note that this is a simplified translation, and you may need to adjust the Python code to make sure it's compatible with the rest of your application.