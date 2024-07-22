In Python, there isn't a direct equivalent of TypeScript's import syntax. The conversion to Python and the `socket.io` (which is a JavaScript library) won't directly map to Python as it depends on the specific Python library being used.

Assuming we are using Flask-SocketIO, the Python code might look something like this:

```python
from flask_socketio import SocketIO, join_room

class Events:
    ROOM_JOIN = 'ROOM_JOIN'

def setup(socketio: SocketIO):
    @socketio.on('connect')
    def on_connect():
        # print("ws connected")
        pass

    @socketio.on(Events.ROOM_JOIN)
    def on_join(data):
        # print("# join room: " + data, request.sid)
        join_room(data)
```

Python doesn't support static type checking like TypeScript does. Hence, the data types are not mentioned in Python. The decorators (`@socketio.on...`) in the Python code correspond to the `.on` functions from the TypeScript code. Please note that this would be different depending on the Python web framework/library used for handling WebSockets.