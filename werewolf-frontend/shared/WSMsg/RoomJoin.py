Python, as a dynamically typed language, does not specify types in its syntax like TypeScript does. Consequently, import modules or defining a message type does not apply the same way it would in TypeScript. However, if you want to define a class to represent `PublicPlayerDef` in python code like you would do with a TypeScript type definition, here's the equivalent:

```python
# public_player_def.py located in the relative directory model_defs
class PublicPlayerDef:
    pass  # Rest of the class implementation here


# somewhere in your Python script, where you want to use your PublicPlayerDef
from model_defs.public_player_def import PublicPlayerDef

class RoomJoinMsg:
    def __init__(self):
        self.public_player_defs = [] # Array to store instances of PublicPlayerDef

# To create instances of PublicPlayerDef and add them to RoomJoinMsg

player_def1 = PublicPlayerDef()
player_def2 = PublicPlayerDef()

room_join_msg = RoomJoinMsg()
room_join_msg.public_player_defs.append(player_def1)
room_join_msg.public_player_defs.append(player_def2)
```
Please modify the `PublicPlayerDef` class code according to your needs. This is just a skeleton. The array (`public_player_defs`) inside the `RoomJoinMsg` class would be equivalent to `PublicPlayerDef[]` in TypeScript.