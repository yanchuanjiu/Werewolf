In Python, we don't have the concept of importing variables and classes from a relative path like in TypeScript or JavaScript, but we'll use the import statements as comments to indicate that these variables and classes are coming from different Python packages/modules. As Python does not support switch or object-like behavior to access global variable values like TIMEOUT[msg.setStatus] we will have to convert it to if...else or dictionary data structures.

Here is the Python translation:

```python
# from "../../shared/GameDefs" import Character, GameStatus, TIMEOUT
# from "../../shared/WSMsg/ChangeStatus" import ChangeStatusMsg
# from "../http/gameGetHint" import getWolfKillResNShow, getWolfsNShow, witchGetDieNShow
# from "../http/gameStatus" import getGameStatus
# from "../reactivity/game" import date, gameStatus, gameStatusTimeLeft, refresh, self

from asyncio import sleep

async def change_status(msg):
    # print("# changeStatus", { "msg": msg })
    date.value = msg.setDay
    gameStatus.value = msg.setStatus

    gameStatusTimeLeft.value = msg.timeout if msg.timeout else TIMEOUT[msg.setStatus]

    await refresh()

    if msg.setStatus == GameStatus.WOLF_KILL_CHECK and self.value.character == "WEREWOLF":
        getWolfKillResNShow()
    elif msg.setStatus == GameStatus.WOLF_KILL and self.value.character == "WEREWOLF":
        getWolfsNShow()
    elif msg.setStatus == GameStatus.WITCH_ACT and self.value.character == "WITCH":
        witchGetDieNShow()
```

This code assumes that refreshing something is asynchronous (uses the asyncio.sleep function). 

Despite this translation, keep understanding that TypeScript modules don't map directly to Python in terms of how they handle files, imports, and executing code. Various TypeScript commands like import from relative path are not usually used in the Python development world. 

Unfortunately, without knowing the context or the function definitions for (refresh, getWolfKillResNShow, getWolfsNShow, witchGetDieNShow) it's hard to provide a fully accurate conversion. Any additional Python functions needed would depend on the implementation of these functions in your original TypeScript code.