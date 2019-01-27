# -*- coding: utf-8 -*-
from typing import cast, List
o = [1]
x = cast(List[int], o)
y = cast(List[None], o)

def foo(obj):
    # type: (object) -> None
    print obj + 5  # Error: can't add 'object' and 'int'
    assert isinstance(obj, int)
    print obj + 5  # OK: type of 'o' is 'int' here
