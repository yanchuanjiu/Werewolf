The equivalent Python code would be:

```python
CLIENT_BASE_URL = "http://werewolf.xiong35.cn"
SERVER_DOMAIN = "http://werewolf.xiong35.cn"
  
SERVER_BASE_URL = SERVER_DOMAIN + "/api"

WS_PATH_CLIPED = "/werewolf-ws"
WS_PATH = "/api" + WS_PATH_CLIPED

IDHeaderName = "player-id"
RoomNumberHeaderName = "room-number"
```
Note that Python uses double or single quotes to specify a string and concatenation is done using the '+' operator. Also, Python does not have an "export" statement like TypeScript, because Python's module system works differently. In Python, you would simply import the required variables from the corresponding Python module.