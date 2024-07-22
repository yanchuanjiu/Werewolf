Here's how the TypeScript code would look in Python:

```python
def get_vote_result(votes):
    vote_situation = get_vote_situation(votes)

    all_targets = list(vote_situation.keys())
    if not all_targets or (len(all_targets) == 1 and all_targets[0] == "0"):
        return None

    max_vote_targets = []
    max_vote_count = float('-inf')

    for target, voters in vote_situation.items():
        if target == "0":
            continue
        if len(voters) < max_vote_count:
            continue
        elif len(voters) == max_vote_count:
            max_vote_targets.append(int(target))
        else:
            max_vote_count = len(voters)
            max_vote_targets = [int(target)]

    return max_vote_targets


def get_vote_situation(votes):
    vote_situation = {}

    for v in votes:
        if not v['voteAt']:
            v['voteAt'] = 0

        if v['voteAt'] not in vote_situation:
            vote_situation[v['voteAt']] = []
        
        vote_situation[v['voteAt']].append(v['from'])

    return vote_situation
```

Note: In Python, we don't need to define the structure of data objects upfront as we do in TypeScript with interfaces (`interface Vote`). Another important thing is in JavaScript and TypeScript accessing an object (dictionary in python) with a key that does not exist will return `undefined` (handled with the || [] part), whereas in Python this would cause a KeyError hence the use of the `dict_keys` function and check if key exists in VoteSituation.