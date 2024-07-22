In Python, below is the equivalent code for the given TypeScript:

Note: Python does not have import statement or exact equivalent for some TypeScript features like async/await and ref keyword. Also Python doesn't support multiple data type like index, Potion in TypeScript. Also Python doesn't support the `undefined` keyword, so it's replaced with `None`.

```python
from enum import Enum

# Assume "vue" reference as Python dictionary,
# and equivalent of `ref(false)` is `{"value": False}`

isActing = {"value": False}
noTarget = {"value": False}
target = {"value": 0}
potion = {"value": None}

class GameStatus(Enum):
    WITCH_ACT = 1
    # other game statuses...

class Potion(Enum):
    POISON = 1
    # other potions...

def characterAct(params):
    # implementation of characterAct function

def showDialog(message, time):
    # implementation of showDialog function

async def act():
    if (
        potion["value"] == Potion.POISON and
        gameStatus["value"] == GameStatus.WITCH_ACT
    ):
        target["value"] *= -1
    
    res = await characterAct({
        "target": target["value"],
    })

    # TODO deal with res

    # hide dialog
    isActing["value"] = False

    if res and res['status'] == 200:
        if 'isWolf' in res['data']:
            showDialog(f"该玩家为{'狼人' if res['data']['isWolf'] else '人类'}", 3)
        else:
            showDialog("操作成功!", 3)

    # reset
    potion["value"] = None
    target["value"] = 0
    noTarget["value"] = False

def setTarget(index):
    if not isActing["value"]:
        return

    target["value"] = index
```
Please adjust this Python code according to the implementations needed for `characterAct` and `showDialog` functions, and the `GameStatus` and `Potion` classes as it wasn't provided in the original TypeScript code.