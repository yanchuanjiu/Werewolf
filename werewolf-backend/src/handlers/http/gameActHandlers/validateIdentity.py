Here's how you would implement the equivalent in Python. Note that Python does not use an equivalent to TypeScript's import statement, switch-case statement, enum type or classes (although Python does have a similar object-oriented structure). It's also important to consider that Python does not have TypeScript's type checking, so we don't need to specify the type of variables.

Also, it's important to consider that Python uses indentation to denote sections of code, so it's crucial to make sure you keep consistent indentation in this code:

```python

GameStatus = {
    "HUNTER_SHOOT": "猎人开枪",
    "SHERIFF_ASSIGN": "指派警长",
    "LEAVE_MSG": "留遗言",
    "WOLF_KILL": "狼人杀人",
    "SEER_CHECK": "预言家查验",
    "WITCH_ACT": "女巫行动",
    "GUARD_PROTECT": "守卫保护",
    "DAY_DISCUSS": "白天讨论",
    "SHERIFF_ELECT": "选举警长",
    "EXILE_VOTE": "放逐投票",
    "SHERIFF_VOTE": "警长投票",
    "SHERIFF_SPEECH": "警长发言"
}

def validateIdentity(room, player):
    gameStatus = room["curStatus"]
    
    if gameStatus == GameStatus["HUNTER_SHOOT"]:
        return player["character"] == "HUNTER" and room["curDyingPlayer"]["_id"] == player["_id"] or "你不是猎人"
        
    elif gameStatus == GameStatus["SHERIFF_ASSIGN"]:
        return player["isSheriff"] and room["curDyingPlayer"]["_id"] == player["_id"] or "你不是警长"
        
    elif gameStatus == GameStatus["LEAVE_MSG"]:
        return player["isDying"] and room["curDyingPlayer"]["_id"] == player["_id"] or "你不能发表遗言"

    if not player["isAlive"]:
        return "你已经是个死人了"

    # Other conditions
    actionStatus = [GameStatus["WOLF_KILL"], GameStatus["SEER_CHECK"], 
                    GameStatus["WITCH_ACT"], GameStatus["GUARD_PROTECT"], 
                    GameStatus["DAY_DISCUSS"], GameStatus["SHERIFF_ELECT"],
                    GameStatus["EXILE_VOTE"], GameStatus["SHERIFF_VOTE"],
                    GameStatus["SHERIFF_SPEECH"]]
                    
    if gameStatus in actionStatus:
        if gameStatus == GameStatus["WOLF_KILL"]:
            return player["character"] == "WEREWOLF" or "你不是狼人"
            
        elif gameStatus == GameStatus["SEER_CHECK"]:
            return player["character"] == "SEER" or "你不是预言家"
            
        elif gameStatus == GameStatus["WITCH_ACT"]:
            return player["character"] == "WITCH" or "你不是女巫"
        
        elif gameStatus == GameStatus["GUARD_PROTECT"]:
            return player["character"] == "GUARD" or "你不是守卫"
        
        elif gameStatus == GameStatus["DAY_DISCUSS"]:
            return player["index"] in room["toFinishPlayers"] or "你不能发言"
        
        elif gameStatus in [GameStatus["SHERIFF_ELECT"], GameStatus["EXILE_VOTE"], GameStatus["SHERIFF_VOTE"]]:
            return True
        
        elif gameStatus == GameStatus["SHERIFF_SPEECH"]:
            return player["canBeVoted"] or "你不能发言"
                    
    return "操作不合法"
```
Remember, in Python, dictionaries are equivalent to JavaScript Objects and Enumerations.

As Python does not have importing files with hierarchy as in JavaScript/TypeScript, you need to design your Python program structure accordingly.