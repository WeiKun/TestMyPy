# -*- coding: utf-8 -*-
from typing import Callable, Iterable, Union, Optional, List, Any

# This is how you annotate a function definition
# 标记函数,标记另起一行
def stringify(num):
    # type: (int) -> str
    """Your function docstring goes here after the type definition."""
    return str(num)

# This function has no parameters and also returns nothing. Annotations
# can also be placed on the same line as their function headers.
# 标记函数在同一行
def greet_world(): # type: () -> None
    print "Hello, world!"

# And here's how you specify multiple arguments
# 多参数标记
def plus(num1, num2):
    # type: (int, int) -> int
    return num1 + num2

# Add type annotations for arguments with default values as though they
# had no defaults
# 带default标记
def default(num1, my_float=3.5):
    # type: (int, float) -> float
    return num1 + my_float

# An argument can be declared positional-only by giving it a name
# starting with two underscores
# 标记禁止指定参数名的调用方式
def quux(__x):
    # type: (int) -> None
    pass

quux(3)  # Fine
#报警内容:error: Unexpected keyword argument "__x" for "quux"
quux(__x=3)  # Error

# This is how you annotate a callable (function) value
x = default  # type: Callable[[int, float], float]

# A generator function that yields ints is secretly just a function that
# returns an iterable (see below) of ints, so that's how we annotate it
# 标记yield生成器
def fIter(n):
    # type: (int) -> Iterable[int]
    i = 0
    while i < n:
        yield i
        i += 1

# There's an alternative syntax for functions with many arguments
# 对每个参数单独打标记，然后在对函数的标记上忽略参数
def send_email(address,     # type: Union[str, List[str]]
               sender,      # type: str
               cc,          # type: Optional[List[str]]
               bcc,         # type: Optional[List[str]]
               subject='',
               body=None    # type: List[str]
               ):
    # type: (...) -> bool
    return True

#test 验证测试
def retFuncIntPass():
    # type: () -> int
    pass                #不报错，应该是mypy对pass的认知并不是返回None，尚不清楚是bug还是特性

def retFuncInt2None():
    # type: () -> int
    return None         #报错

def retFuncInt2Str():
    # type: () -> int
    return ''           #报错

#推算标记
intV = retFuncIntPass()
intV = ''               #报错，因为对retFuncIntPass的调用已经将intV递归标注为int了

#推算标记
strV = '' # type: str
strV = retFuncIntPass() #报错，因为strV的标注不符合retFuncIntPass的返回类型

def no_mark_func(arg):
    a = arg
    b = 1 # type: int   
    b = ''              #不报错，因为没标注函数本身，因此不会对函数内部进行检查
    return

def mark_func(arg):
    # type: (Any) -> Any
    a = 1 # type: int
    a = ''              #报错
    return

no_mark_func(1)


