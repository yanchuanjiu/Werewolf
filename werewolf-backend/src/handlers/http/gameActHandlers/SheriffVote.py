Python doesn't have a direct equivalent of TypeScript's import syntax or the decorators. Unlike TypeScript, Python doesn't have static typing. As such, there will be significant differences between the two codes. A Python script matching the structure and program flow of your given TypeScript example would look something like this:

```python
from models import Player, Room
from utils import get_vote_result, render_hint_n_players
from handlers import GameActHandler, start_current_state, SheriffSpeachHandler, SheriffVoteCheckHandler
from shared import GameStatus, Events
from errors import create_error

class SheriffVoteHandler(GameActHandler):
  def __init__(self):
    self.cur_status = GameStatus.SHERIFF_VOTE

  async def handle_http_in_the_state(self, room, player, target, ctx):
    if not room.get_player_by_index(target).can_be_voted:
      create_error(status=400, msg="选择的玩家未参与竞选")

    if player.can_be_voted:
      create_error(status=400, msg="参选者不能投票")

    player.sheriff_votes[0] = target

    return {
      'status': 200,
      'msg': 'ok',
      'data': {'target': target},
    }

  def start_of_state(self, room):
    start_current_state(self, room)

  async def end_of_state(self, room):
    votes = [{'from': p.index, 'vote_at': p.sheriff_votes[0]} for p in room.players]
    highest_votes = get_vote_result(votes)

    if not highest_votes or len(highest_votes) == 0:
      io.to(room.room_number).emit(Events.SHOW_MSG, {'innerHTML': "所有人都弃票, 即将进入自由发言阶段"})
      return SheriffVoteCheckHandler.start_of_state(room)
    elif len(highest_votes) == 1:
      room.get_player_by_index(highest_votes[0]).is_sheriff = True
      io.to(room.room_number).emit(Events.SHOW_MSG, {'innerHTML': render_hint_n_players("当选警长的玩家为:", highest_votes)})
      return SheriffVoteCheckHandler.start_of_state(room)
    else:
      room.to_finish_players = set()
      for p in room.players:
        if p.index in highest_votes:
          p.can_be_voted = True
          room.to_finish_players.add(p.index)
        else:
          p.can_be_voted = False
          p.sheriff_votes[0] = None
      io.to(room.room_number).emit(Events.SHOW_MSG, {'innerHTML': render_hint_n_players("竞争警长的玩家如下, 请再次依次进行发言", highest_votes)})
      return SheriffSpeachHandler.start_of_state(room)
```

Notes: 

1) The `import` statements at the top of the Python script are made-up and not guaranteed to be correct. The exact translation would depend on how your project is structured and where the modules to import are located in your project.

2) Similarly, the functions/classes referred in the code like `GameActHandler`, `start_current_state`, `SheriffSpeachHandler`, `SheriffVoteCheckHandler`, `get_vote_result`, `render_hint_n_players` etc need to be defined somewhere in your Python project.

3) `async` and `await` keywords in Python are used for asynchronous programming. They allow you to write concurrent code using a more direct style of syntax and structure, avoiding callbacks. The function using `await` must be decorated with `async`. 

4) In Python, the `self` keyword is used to represent an instance of the class. It binds the attributes with the given arguments. Inside a class method, you'd use it like this: `self.sheriff_votes`. 

Please adjust the code according to your requirements and project structure.