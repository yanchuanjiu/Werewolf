In Python, we use the library `socketIO-client-nexus` for websocket client connections. We don't have static typing like `let socket: SocketIOClient.Socket;` and don't have in-built module system like in TypeScript, so we'll handle modules with Python's own import system, which lets us use any installed packages. For example, if we have constants and WSEvents classes in the folders `shared.constants` and `shared.WSEvents`, we can import it using python's import system as `from shared.constants import SERVER_DOMAIN, WS_PATH` and `from shared.WSEvents import Events`. Also 'handlers' are simply methods in python, which we can define in our program or import from other python files.

Here is your code translated into Python:

```python
from socketIO_client_nexus import SocketIO

from shared.constants import SERVER_DOMAIN, WS_PATH
from shared.WSEvents import Events

# handlers - assuming that handlers are in the same directory
from changeStatus import changeStatus
from gameBegin import gameBegin
from gameEnd import gameEnd
from roomJoin import roomJoin
from showWSMsg import showWSMsg

socket = None

def joinRoom(roomNumber):
    global socket
    if socket:
        socket.disconnect()

    socket = SocketIO(SERVER_DOMAIN, None, path = WS_PATH)

    socket.on("connection", lambda: print("#ws connected"))
    socket.on(Events.CHANGE_STATUS, changeStatus)
    socket.on(Events.GAME_BEGIN, gameBegin)
    socket.on(Events.GAME_END, gameEnd)
    socket.on(Events.ROOM_JOIN, roomJoin)
    socket.on(Events.SHOW_MSG, showWSMsg)

    socket.emit(Events.ROOM_JOIN, roomNumber)

# In python, we don't need to explicitly export. 
# Any other python program can just import this file to get access to these variables and functions.
```

Note: `socketIO-client-nexus` is a websocket library for python. If the handlers are in different directories, be sure to adjust the imports accordingly to follow Python's import conventions. Make sure the handlers are implemented as functions in their respective files.