In Python, you'd accomplish the same operations but some concepts like 'Middleware', 'Room.getRoom', 'getPlayerById' and importing/exporting modules are specific to TypeScript or Node.js. While translating the given code snippet, we'd need to implement customized methods or classes to handle these features which Python does not inherently support.

Here's a basic translation:

```python
from .constants import IDHeaderName, RoomNumberHeaderName
from .RoomModel import Room

class UseAuth:
    @staticmethod
    async def __call__(ctx, next):
        if ctx.method != "OPTIONS":
            playerID = ctx.get(IDHeaderName)
            roomNumber = ctx.get(RoomNumberHeaderName)

            room = Room.getRoom(roomNumber)
            if room is not None:
                room.getPlayerById(playerID)

        await next()

useAuth = UseAuth()
```
Please note that you would have to define the 'get method in 'ctx' object pased as argument, and also define 'getRoom' and 'getPlayerById' methods inside the 'Room' class. Python doesn't directly support the import/export module feature in the same way as JavaScript/TypeScript. The data types used in Python may also vary depending upon what 'IDHeaderName', 'RoomNumberHeaderName' are, and what is returned by 'Room.getRoom' and 'room.getPlayerById'. Similarly, Python does not directly support TypeScript's optional chaining ('?.'). Instead, in Python you would usually check if the object is not None before calling a method on it, as shown in the translation. 

Given Python functions are not inherently asynchronous, for the async-await to work, you need to run this in an event loop with the help of an asyncio library.