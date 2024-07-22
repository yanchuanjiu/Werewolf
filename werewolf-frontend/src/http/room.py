Python does not have the concept of TypeScript's async and await out of the box. But asyncio library simulates this, and aiohttp library can be used for async http requests. Note that typing in Python is optional and does not enforce type safety like TypeScript.

Here is your TypeScript code translated to Python:

```python
from typing import Optional
from aiohttp import ClientSession
from . import _request

async def create_room(data: 'CreateRoomRequest') -> 'CreateRoomResponse':
    async with ClientSession() as session:
        res = await _request(session, {
            'url': "/room/create",
            'method': "POST",
            'data': data,
        })

    return res

async def join_room(data: 'JoinRoomRequest') -> Optional['JoinRoomResponse']:
    async with ClientSession() as session:
        res = await _request(session, {
            'url': "/room/join",
            'method': "POST",
            'data': data,
        })

    return res

async def init_room(data: 'InitRoomRequest') -> Optional['InitRoomResponse']:
    async with ClientSession() as session:
        res = await _request(session, {
            'url': "/room/init",
            'method': "POST",
            'data': data,
        })

    return res

async def game_begin() -> bool:
    async with ClientSession() as session:
        res = await _request(session, {
            'url': "/game/begin",
            'method': "POST",
        })

    return res.status == 200
```

Note: The `_request` function should be defined in your '_request' python file and the input argument 'session' should be an instance of `ClientSession`. GraphQL types 'CreateRoomRequest', 'CreateRoomResponse', 'JoinRoomRequest', 'JoinRoomResponse', 'InitRoomRequest', 'InitRoomResponse' should be defined before they can be used in the type hints. 'Optional' indicates that the function can also return None.