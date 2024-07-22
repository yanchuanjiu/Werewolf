Python doesn't inherently support TypeScript's strong typing and object-oriented syntax. However, Python does have built-in support for classes and can mimic some TypeScript features using the classes and Dictionaries objects.

Here is the Python code:

```python
import time
import re
import datetime
from typing import List, Dict
from collections import defaultdict

roomMap = {}

class Room:
  def __init__(self, creator, needingCharacters, password = None):
    if not checkNeedingCharacters(needingCharacters):
      raise Exception('人数配比不合法')
    tryTime = 20
    while tryTime > 0:
      roomNumber = str(hash(time.time()))[0:6]
      prevRoom = roomMap.get(roomNumber, None)
      if prevRoom and (datetime.datetime.now() - prevRoom["createdAt"]).total_seconds() < 86400:
        continue
      
      self.creatorID = creator.get('_id')
      self.players = [creator]
      self.needingCharacters = needingCharacters
      self.remainingIndexes = list(range(2, len(needingCharacters)))
      roomMap[self.creatorID] = self
      break
      
    if tryTime <= 0:
      raise Exception('创建错误, 请重试!')
        
  def playerJoin(self, name, password = None):
    nameReg = re.compile(".{1,15}")
    if not nameReg.match(name):
      raise Exception('昵称不合法')
    if self.password and self.password != password:
      raise Exception('密码错误')
    if len(self.remainingIndexes) == 0:
      raise Exception('房间已满')

    index = self.remainingIndexes.pop(0)
    player = Player(name, index)

    self.players.append(player)

    return player

  def choosePublicInfo(self):
    self.players.sort(key = lambda x: x.get('index'))
    return self.players

  def getPlayerById(self, id):
    for player in self.players:
      if player.get('_id') == id:
        return player
    raise Exception('id 错误')

  def getPlayerByIndex(self, index):
    for player in self.players:
      if player.get('index') == index:
        return player
    raise Exception('编号错误')

  @staticmethod
  def getRoom(number):
    if number in roomMap:
      return roomMap[number]
    raise Exception('未找到房间号')
      
  @staticmethod
  def clearRoom(number):
    if number in roomMap:
      del roomMap[number]

def checkNeedingCharacters(needingCharacters):
  if len(needingCharacters) == 0:
    return False
  charMap = defaultdict(int)
  for character in needingCharacters:
    charMap[character] += 1
  if 'WEREWOLF' not in charMap:
    return False
  if charMap['WEREWOLF'] > len(needingCharacters) / 2:
    return False
  return True
```

Please note that this is a rough translation, and some modifications may needed to make it runnable based on your definitions of certain classes like Character, Player etc. You also need to declare the Player class beforehand, and consider to make ID and password properties of Player class.