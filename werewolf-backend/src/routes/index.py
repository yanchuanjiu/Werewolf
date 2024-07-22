Python, especially using its popular web framework Flask, doesn't directly map 1:1 with TypeScript and the Koa-router module, as they have different ways of handling and organizing routers, middleware, and routes. However, your TypeScript code can be translated into analogous Python code using the Flask framework like this:

```python
from flask import Flask
from flask_httpauth import HTTPBasicAuth
from .middleware.auth import UseAuth
from .t import test
from .gameRoutes import gameRoutes
from .roomRoutes import roomRoutes

app = Flask(__name__)
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    # add your password check logic here
    return UseAuth(username, password)

@app.route('/test', methods=['GET', 'POST', 'PUT', 'DELETE'])
def test_route():
    return test()

app.register_blueprint(roomRoutes, url_prefix='/room')
app.register_blueprint(gameRoutes, url_prefix='/game')
```

This Python code assumes authentication is checked using an HTTP Basic Auth mechanism. You will need to adjust verify_password function according to your needs.

Also, roomRoutes and gameRoutes should be blueprints in Python:

gameRoutes.py:

```python
from flask import Blueprint

gameRoutes = Blueprint('gameRoutes', __name__)

# define your routes here
```

roomRoutes.py:

```python
from flask import Blueprint

roomRoutes = Blueprint('roomRoutes', __name__)

# define your routes here
```
You will need to define the routes and functionalities inside these blueprint files. There is no direct analog for the `.routes()` and `.allowedMethods()` methods used in Koa-router.

Assuming that the `test` method is similar to how routes are defined in Flask, I created a route for '/test' that can respond to all types of HTTP requests (GET, POST, PUT, DELETE). It calls the `test` function from t.py. You can adjust this based on your actual needs.