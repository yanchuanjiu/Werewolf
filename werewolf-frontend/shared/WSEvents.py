Python does not have built-in support for enums, but the functionality can be achieved using a class:

```python
class Events:
    # Room related
    ROOM_EXILE = "ROOM_EXILE"  # Kicked out of the room
    ROOM_JOIN = "ROOM_JOIN"  # Someone joins the room
    GAME_BEGIN = "GAME_BEGIN"  # Start the game
    GAME_END = "GAME_END"  # End the game

    # Game related
    CHANGE_STATUS = "CHANGE_STATUS"  # Set the current status of the game
    NOTICE_GET_STATUS = "NOTICE_GET_STATUS"  # Request for role info // TODO
    SHOW_MSG = "SHOW_MSG"  # Messages pushed from the backend to the frontend
```