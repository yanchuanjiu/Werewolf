Python does not have a direct equivalent to Vue3's reactive programming model, so we need to work around this. Here is a basic conversion:

```python
dialogTimeLeft = 0
toShowContents = []
content = None

def update_content():
    global content
    if len(toShowContents) > 0:
        content = toShowContents[0]
    else:
        content = None

"""
Function to show a popup for a certain time period, default to 5 seconds
@param toShowContent: the text to show (supports HTML)
@param showTime: the duration to show the text
"""
def showDialog(toShowContent, showTime = 5):
    toShowContents.append({
        "content": toShowContent,
        "timeout": showTime
    })
    update_content()
```

Here, we are maintaining the reactive behavior with a function (`update_content`), which sets the `content` variable to match how it would behave in the original TypeScript. `showDialog` updates `toShowContents` then calls `update_content` to update `content`.