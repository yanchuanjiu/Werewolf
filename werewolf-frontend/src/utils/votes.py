Here's the Python translation of your TypeScript code:

```Python
from typing import List, Dict

class Vote:
    def __init__(self, from_index, vote_at):
        self.from_index = from_index
        self.vote_at = vote_at if vote_at else 0

def get_vote_situation(votes: List[Vote]) -> Dict[int, List[int]]:
    vote_situation = {}

    for v in votes:
        if not v.vote_at:
            v.vote_at = 0

        if v.vote_at not in vote_situation:
            vote_situation[v.vote_at] = []
            
        vote_situation[v.vote_at].append(v.from_index)

    return vote_situation
```

In the Python translation:
1. We define a class `Vote` to mimic the TypeScript interface, and we replace the property `from` with `from_index` because `from` is a reserved keyword in Python.
2. As Python doesn't have static types, `index` in the original TypeScript code is replaced with `int` in Python's type hints.
3. Python doesn't have a direct equivalent to TypeScript's `Record` type. The Python typing `Dict` is used instead.