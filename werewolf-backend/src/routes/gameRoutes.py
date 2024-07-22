There are some tasks that need to be accomplished before the TypeScript can be translated to Python.

Python does not have the exact equivalents for the `import`, `export`, `const` keywords, decorator methods (like `post` or `use`) and classes (like `Router`).

The concise code of TypeScript that implements a HTTP server using the `koa-router` library would be quite verbose and harder to follow in Python. 

As per the use cases, `Flask` is a popular library in Python to create HTTP servers. The below is a very basic translation to Flask:

First we have to install `Flask` using pip:

```
pip install flask
```

```python
from flask import Flask, request
from handlers.http import gameAct
from handlers.http import gameBegin
from handlers.http import gameGetHint
from handlers.http import gameStatus

app = Flask(__name__)

@app.route("/begin", methods=["POST"])
def begin_game():
    return gameBegin()

@app.route("/status", methods=["POST"])
def status_game():
    return gameStatus()

@app.route("/act", methods=["POST"])
def act_game():
    return gameAct()

@app.route("/hint", methods=["GET", "POST"])
def get_hint():
    return gameGetHint()

# TODO get vote result
# TODO 各个玩家在自己回合开始时检查自己能干嘛, 如女巫看看昨晚谁死了, 守卫看看自己昨晚保的谁

if __name__ == "__main__":
    app.run(port=5000)
```

I couldn't convert `hintResultRouter.routes()` and `hintResultRouter.allowedMethods()` as they depend on how `hintResultRouter` is defined, but in Flask you just declare the route and then list the allowed HTTP methods. 

This Flask server handling HTTP will be started by running the Python script and will listen on http://localhost:5000.