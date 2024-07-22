import hashlib
from vue import reactive, ref

from shared.GameDefs import SetableCharacters
from http.room import createRoom
from router import router
from socket import joinRoom
from utils.token import setToken
from dialog import showDialog
from game import needingCharacters, players

characters = reactive({
  "GUARD": 1,
  "HUNTER": 1,
  "SEER": 1,
  "VILLAGER": 2,
  "WEREWOLF": 3,
  "WITCH": 1,
})

def setCharacter(character: SetableCharacters, type: int) -> bool:
  if characters[character] + type < 0:
    return False
  if character in ["SEER", "HUNTER", "GUARD", "WITCH"]:
    if type == 1 and characters[character] == 1:
      return False
  characters[character] += type
  return True

nickname = ref("")
password = ref("")

async def create():
  if not nickname.value:
    return showDialog("请填写昵称")

  characterNames = []
  for _name in characters.keys():
    name = _name
    characterNames += [name] * characters[name]
  needingCharacters.value = characterNames

  sh = hashlib.sha256()
  if password.value:
    sh.update(password.value.encode())
    hashed_password = sh.hexdigest()
  else:
    hashed_password = None

  res = await createRoom(characters=characterNames, name=nickname.value, password=hashed_password)
  
  if res and res.status == 200:
    data = res.data
    joinRoom(data.roomNumber);

    showDialog("创建成功, 进入等待房间")
    router.push(name="waitRoom", query={"pw": password.value, "number": data.roomNumber})
    setToken(data.ID, data.roomNumber)

    players.value = [{
        "index": 1,
        "isAlive": True,
        "name": nickname.value,
        "isSheriff": False,
        "isDying": False,
        "hasVotedAt": [],
        "sheriffVotes": [],
    }]