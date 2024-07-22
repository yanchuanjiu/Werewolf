Python doesn't have a direct equivalent to TypeScript's import syntax, but assuming that `RoomJoinMsg` is a class or function and `players` is a module in Python, you might import and use them in Python like so:

```python
from shared.WSMsg.RoomJoin import RoomJoinMsg
import reactivity.game as game

def room_join(msg: RoomJoinMsg):
    # print("#ws on room join")

    game.players.value = msg
```

However, Python does not support TypeScript features such as type annotation, so `msg: RoomJoinMsg` is not valid Python syntax. In Python, you wouldn't specify the type of `msg` upon function definition. 

Another thing to note is that setting properties like `game.players.value` may not work the same way in Python as it does in TypeScript, depending on how the `players` object is defined. This is due to difference in the way TypeScript and Python handle object-oriented programming.