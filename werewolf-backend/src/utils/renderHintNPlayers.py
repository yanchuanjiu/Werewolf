Here is the Python code equivalent to the provided TypeScript code:

```python
def render_hint_n_players(hint, players=None):
    player_HTML = ""
    if players:
        for index in players:
            player_HTML += """
            <div class="die-player">
              <div class="die-player-index">{}</div>号
            </div>
            """.format(index)
    inner_HTML = """
          <style>
            .die-player-wrapper {
              display: flex;
              margin-top: 10px;
            }
          
            .die-player-wrapper .die-player {
              display: flex;
              align-items: flex-end;
              margin: 5px;
            }
          
            .die-player-wrapper .die-player .player-index {
              width: 40px;
              height: 40px;
              line-height: 40px;
              text-align: center;
              border-radius: 999px;
              background-color: var(--on-bg);
              color: var(--bg);
            }
          </style>
          <div>{}</div>
          <div class="die-player-wrapper">
            {}
          </div>
          """.format(hint, player_HTML)
    return inner_HTML
```

Notice the `{}` replacements in the Python version compared to the `${}` in the TypeScript version. They are used for the `format` method in Python.