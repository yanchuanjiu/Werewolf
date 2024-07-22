Python does not have an equivalent for TypeScript's import-as syntax, and it also does not use the concept of "exporting" functions. However, below is a Python function that mirrors the functionality of your provided TypeScript code as closely as possible:

from reactivity.joinRoom import gameBegin as begin

def game_begin():
  # print("#ws on game begin")

  begin()