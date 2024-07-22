In Python, there isn't a direct translation for TypeScript's `interface` and `type` but we can use class or dataclass to depict the object structure. Here's the equivalent Python code:

```python
from dataclasses import dataclass
from typing import Optional, List
from "../GameDefs" import Character
from "../ModelDefs" import ID, index
from "./_httpResTemplate" import HttpRes

@dataclass
class JoinRoomRequest:
    name: str  #昵称
    password: Optional[str] = None  #哈希过的密码
    roomNumber: str  #六位房间号

@dataclass
class JoinRoomResponse(HttpRes):
    ID: ID  # token
    index: index
    needingCharacters: List[Character]  #设置的人物
```

Note: 
1. Python uses snake_case naming convention as opposed to camelCase in TypeScript. So, "roomNumber" becomes "room_number" etc.
2. Python uses None instead of undefined in TypeScript. So, "password?: string;" becomes "password: Optional[str] = None" in Python.
3. Python uses "from...import..." import style. Ensure that relevant dependencies (such as Character, ID, index and HttpRes) exist or are correctly defined/importable from the paths provided.
4. Annotations like "//昵称" or "//设置的人物" can be added as comments in Python.
5. Python does not have TypeScript's type keyword. A python dataclass that inherits from HttpRes has been created in this context. Make sure that makes logical sense in your actual use case.