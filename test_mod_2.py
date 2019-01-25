# -*- coding: utf-8 -*-
from typing import List, Set, Dict, Tuple, Text, Optional, Callable
import test_mod_1

test_mod_1.functionA('')        #报错
testA = test_mod_1.Base()
testA.functionA('')             #报错

@test_mod_1.decoratorA
def func(arg):
    # type: (str) -> None
    return

func('')                        #报错


class TestClass(object):
    def __int__(self):
        # type: () -> None
        pass


def test_funcA():
    # type: () -> None
    import test_mod_0
    a = test_mod_0.TestClassA()
    a.attrA = ''                #报错

