Python does not use TypeScript's type declaration syntax or its module import syntax. Here is how the TypeScript code you provided could be translated into Python using the requests library:

```python
import requests
from .reactivity_dialog import showDialog
"""
Get the result of the werewolf killing and display a dialog
@return whether it was successful
"""
def getWolfKillResNShow():
  res = requests.get("/game/hint/wolfKill")

  if not res or res.status_code != 200:
    return False

  showDialog(res.text)

  return True

"""
Get the wolf teammates and display a dialog
@return whether it was successful
"""
def getWolfsNShow():
  res = requests.get("/game/hint/getWolfs")

  if not res or res.status_code != 200:
    return False

  showDialog(res.text)

  return True

"""
The witch gets the result of the werewolf killing and displays a dialog
@return whether it was successful
"""
def witchGetDieNShow():
  res = requests.get("/game/hint/witchGetDie")

  if not res or res.status_code != 200:
    return False

  showDialog(res.text)

  return True
```
In this conversion, I've also replaced the request function from your original TypeScript code with requests.get(), part of the Python requests library. Please replace it with actual function if you have a different implementation. Note that Python does not natively support async/await syntax, you will need to use asyncio library for asynchronous tasks which is not used above as tasks seems independent.

Additionally, showDialog function is assumed to be a function that takes a string argument. Please adjust as necessary based on its actual implementation.