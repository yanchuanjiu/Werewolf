Python, specifically Flask, handles routing differently than TypeScript. Here's how you could potentially translate the code:

```python
from flask import Flask
from getWolfs import get_wolfs
from witchGetDie import witch_get_die
from wolfKill import get_wolf_kill_result

app = Flask(__name__)

@app.route('/wolfKill', methods=['GET'])
def wolf_kill():
    return get_wolf_kill_result()

@app.route('/witchGetDie', methods=['GET'])
def witch_die():
    return witch_get_die()

@app.route('/getWolfs', methods=['GET'])
def wolves():
    return get_wolfs()

if __name__ == '__main__':
    app.run(debug=True)
```

Please ensure to have the function `get_wolf_kill_result`, `get_wolfs`, `witch_get_die` in their respective python files (`getWolfs.py`, `wolfKill.py`, `witchGetDie.py`). If you want, you can combine them in one file.

Note: In python, it's more common to use snake_case (`get_wolfs` instead of `getWolfs`) for function names, variable names and file names. Python does not have a feature like export default in TypeScript. Therefore, the export default statement is not translated.