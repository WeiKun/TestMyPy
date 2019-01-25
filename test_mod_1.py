# -*- coding: utf-8 -*-
from typing import List, Set, Dict, Tuple, Text, Optional, Callable


def functionA(arg):
    # type: (int) -> None
    return

class Base(object):
    def __init__(self):
        # type: () -> None
        pass

    def functionA(self, arg):
        # type: (int) -> None
        return

def decoratorA(func):
    # type: (Callable) -> Callable[[int], None]
    def newfunc(arg):
            return

    return newfunc
