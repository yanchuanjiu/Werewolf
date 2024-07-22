Python does not have a feature equivalent to TypeScript's localStorage. Instead, persistence in Python is typically achieved using filesystem I/O operations or databases. 

Here's an analogous translation of the TypeScript code using Python's built-in JSON module for serialization/de-serialization and filesystem for storage.

```python
import json
import os

ROOM_NUMBER_PREFIX = "WERE_WOLF_ROOM"
ROOM_LIST_KEY = "WERE_WOLF_ROOMS"

class RoomRecordBrief:
    def __init__(self, time :int, roomNumber :str):
        self.time = time
        self.roomNumber = roomNumber

class RoomRecord(RoomRecordBrief):
    def __init__(self, time :int, roomNumber :str, groupedGameEvents :list, playerBriefs :list, selfIndex :int):
        super().__init__(time, roomNumber)
        self.groupedGameEvents = groupedGameEvents
        self.playerBriefs = playerBriefs
        self.selfIndex = selfIndex

def getKeyByNumberNTime(roomNumber: str, time: int) -> str:
    return f"{ROOM_NUMBER_PREFIX}-{roomNumber}-{time}"

def saveRecord(groupedGameEvents :list, roomNumber :str, self :dict, players :list, time :int):
    recordBrief = RoomRecordBrief(time, roomNumber)

    playerBriefs = [{ "name": p['name'], "index": p['index'], "character": p['character']} for p in players]
    record = RoomRecord(time, roomNumber, groupedGameEvents, playerBriefs, self['index'])

    with open(getKeyByNumberNTime(roomNumber, time) + '.json', 'w') as file:
        json.dump(record.__dict__, file)
  
    prevRoomList = []

    if os.path.exists(ROOM_LIST_KEY + '.json'):
        with open(ROOM_LIST_KEY + '.json', 'r') as file:
            prevRoomList = json.load(file)

    prevRoomList.append(recordBrief.__dict__)
    with open(ROOM_LIST_KEY + '.json', 'w') as file:
        json.dump(prevRoomList, file)

def getAllRecords() -> list:
    with open(ROOM_LIST_KEY + '.json', 'r') as file:
        return json.load(file)

def getRecordByNumberNTime(roomNumber :str, time :int):
    if os.path.exists(getKeyByNumberNTime(roomNumber, time) + '.json'):
        with open(getKeyByNumberNTime(roomNumber, time) + '.json', 'r') as file:
            return json.load(file)
    
    return None
```

Please note that the 'useAllRecords' and 'useRecord' function do not have a perfect analogy in Python as they are leveraging Vue.js specific features for Vue components which doesn't exist in Python.