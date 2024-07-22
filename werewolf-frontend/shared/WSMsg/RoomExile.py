In Python, there's no direct equivalent to TypeScript's type alias feature. Python is a dynamically typed language, so we don't usually define variable types as we do in TypeScript, a statically typed language. 

However, recently Python has introduced some features to optionally provide type information, generally used for static type checking, but it doesn't have a direct equivalent of TypeScript or JavaScript imports. Considering that, the concept you're trying to convey can be represented in Python using class definitions if you want to maintain information about the structure of data.

Firstly, I'll assume that `PublicPlayerDef` is a class defined in the module `ModelDefs`. Here's how you might define an equivalent `PublicPlayerDef` class in Python:

from ModelDefs import PublicPlayerDef

To define `RoomExileMsg` as a list of `PublicPlayerDef` objects, you can use Python's typing module to define a type hint, but remember that this is optional and mainly for the benefit of static type checkers, IDEs, linters, etc. Python won't enforce this typing at runtime.

from typing import List

RoomExileMsg = List[PublicPlayerDef]

After this point, you can use `RoomExileMsg` as a type hint in your function definitions, to indicate that a function expects a list of `PublicPlayerDef` objects.