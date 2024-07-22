In Python, we don't have direct equivalents for `import * as` from TypeScript. Also, Node.js router pattern isn't directly applicable to Python. However, with Flask, a popular web framework in Python, we can achieve roughly the same outcomes. The following is a Python code using Flask equivalent of your TypeScript code.

This assumes that roomCreate, roomJoin and roomInit are functions that needs to be implemented.

```python
from flask import Flask, request
app = Flask(__name__)

@app.route('/create', methods=['POST'])
def room_create():
    # roomCreate implementation goes here
    pass

@app.route('/join', methods=['POST'])
def room_join():
    # roomJoin implementation goes here
    pass

@app.route('/init', methods=['POST'])
def room_init():
    # roomInit implementation goes here
    pass

if __name__ == "__main__":
    app.run(debug=True)
```

Remember to implement the necessary functionality in the room_create, room_join, and room_init functions.