In Python, you would not import individual functions, as in TypeScript. The Python equivalent to the above code will involve the definition of the function and variable assignments, which could look something like the following, but depends heavily on how the "reactivity" code is implemented or structured in the Python side.

```python
from reactivity import playAction, playPage

# Each operation needs to do, such as closing operation panels, etc.
def commonAction(no_target):
    playPage.showActions.value = False
    playAction.isActing.value = True
    playAction.target.value = -1
    playAction.noTarget.value = no_target
```

Note that this will only work if `showActions`, `isActing`, `target`, and `noTarget` are attributes of the imported `playAction` and `playPage` modules and have a `value` property.

If `showActions`, `isActing`, `target`, and `noTarget` are global variables in their respective modules, the Python version would look something like this:

```python
import reactivity.playAction as playAction
import reactivity.playPage as playPage

# Each operation needs to do, such as closing operation panels, etc.
def commonAction(no_target):
    playPage.showActions = False
    playAction.isActing = True
    playAction.target = -1
    playAction.noTarget = no_target
```

It's important to note that TypeScript's importing ability does not have a direct equivalent in Python when it comes to manipulating other script's variables. Python's architecture discourages manipulation of another script's variables for the sake of good programming practice and encapsulation.