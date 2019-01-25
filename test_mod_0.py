# -*- coding: utf-8 -*-
from typing import List, Set, Dict, Tuple, Text, Optional, Callable
import test_mod_2

class TestClassA(test_mod_2.TestClass):
    def __int__(self):
        # type: () -> None
        self.attrA = 10

    def funcA(self, arg):
        # type: (str) -> None
        pass
