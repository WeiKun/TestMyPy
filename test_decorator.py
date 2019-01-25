# -*- coding: utf-8 -*-
from typing import List, Set, Dict, Tuple, Text, Optional, Callable

#不生效
def test_decoratorA(func):
    def newfunc(arg):
        # type: (str) -> None
        return

    return newfunc

#生效
def test_decoratorB(func):
    # type: (Callable) -> Callable[[str], None]
    def newfunc(arg1, arg2):
        # type: (int, int) -> None
        return

    return newfunc      #报错，因为不符合test_decoratorB的标注

#依然会洗去函数特性
def test_decoratorC(func):
    return func

@test_decoratorA
def testFuncA(arg):
    # type: (int) -> None
    return

@test_decoratorB
def testFuncB(arg):
    # type: (int) -> None
    return

@test_decoratorC
def testFuncC(arg):
    # type: (int) -> None
    return

testFuncA(None) #啥都不报,因为test_decoratorA抹去了标注
testFuncB(None) #报错,根据test_decoratorB的标注
testFuncC(None) #啥都不报,因为test_decoratorC抹去了标注
