# -*- coding: utf-8 -*-

import sys;
sys.path.append("../testfolder1/")

from typing import List, Set, Dict, Tuple, Text, Optional, Callable
import test_mod_1

test_mod_1.functionA('')
testA = test_mod_1.Base()
testA.functionA('')

@test_mod_1.decoratorA
def func(arg):
    # type: (str) -> None
    return

func('')
