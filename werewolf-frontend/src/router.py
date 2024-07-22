Python doesn't have a direct equivalent for Vue, so translating Vue Router from TypeScript to Python isn't possible.

The code you have given seems like it's setting up routes for a Vue JS application which is a JavaScript framework for building user interfaces.

Python equivalents would include frameworks like Django or Flask, but the routing and overall structure of these is quite different, and not directly translatable. There is no 'import component from vue-file' equivalent in Python since Python (being a backend language) doesn't have a built-in concept of "components" like in frontend frameworks.

Take this as an example, routing in Flask may look like this:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/createRoom')
def create_room():
    return render_template('createRoom.html')

# ... rest of your routes
```

You can create HTML templates in a templates directory and pass variables to them from your route functions. This isn't exactly the same as what you're doing in Vue, but it's the closest equivalent in Python with Flask. Django has a similar structure.

Remember that while TypeScript is used for front-end development, Python is generally used for back-end development. Hence, many concepts from front-end development (like dealing with Vue or React components) don't have a direct corresponding concept in Python.