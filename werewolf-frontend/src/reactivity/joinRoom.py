The Python code equivalent to the provided TypeScript code would be as follows:

```python
from hashlib import sha256
from flask import redirect, url_for
from .room import join_room as join_room_http
from .socket import Events, join_room as join_room_socket
from .token import get_token, set_token
from .dialog import show_dialog

room_number = ""
password = ""
nickname = ""

def join():
    global room_number, password, nickname
    if not room_number:
        return show_dialog("请填写房间号")
    if not nickname:
        return show_dialog("请填写昵称")
    
    password_hash = sha256(password.encode()).hexdigest() if password else None
    res = join_room_http(room_number, nickname, password_hash)

    if res and res.status_code == 200:
        join_room_socket(room_number)

        show_dialog("成功加入房间!")
        needing_characters = res.json['needingCharacters']
        
        set_token(res.json['ID'], room_number)
        
        return redirect(url_for('waitRoom', pw=password, number=room_number))

def game_begin():
    import local_storage
    local_storage.remove_item("memo")
    show_dialog("游戏开始, 天黑请闭眼👁️")
    import time
    time.sleep(0.5)
    return redirect(url_for('play'))
```

Note: For TypeScript's router push, Python is using Flask's redirect with url_for. See [Flask documentation](https://flask.palletsprojects.com).

Also, Python doesn't have a local storage like browser-based JavaScript, so you'd need a Python equivalent for localStorage. Here, I am importing a fictional `local_storage` but the specific way to remove local saved information would depend on how you have designed your Python environment.