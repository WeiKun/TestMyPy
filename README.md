# mypy使用心得
## 参考资料
https://mypy.readthedocs.io/en/latest/cheat_sheet.html

https://github.com/python/mypy/blob/master/README.md

## 安装
1. sudo apt-get install python3 python3-pip
2. sudo python3 -m pip install -U git+git://github.com/python/mypy.git
    或者 sudo python3 -m pip install mypy

## 使用
mypy --py2 xxx.py

## 普通用例介绍

根据[官方用例](https://mypy.readthedocs.io/en/latest/cheat_sheet.html)进行验证跟扩展尝试

### built in类型
#### 使用方法

```python
# -*- coding: utf-8 -*-
from typing import List, Set, Dict, Tuple, Text, Optional

# 标注基础类型
intV = 1  # type: int
floatV = 1.0  # type: float
boolV = True  # type: bool
strV = "test"  # type: str
unicodeV = u"test"  # type: unicode
noneV = None    # type: None

# 标注list/set
listV = [1]  # type: List[int]
setV = {6, 7}  # type: Set[int]

# 标注dict,可以指定key/value类型
dictV = {'field': 2.0}  # type: Dict[str, float]

# 标注tuple
tupleV = (3, "yes", 7.5)  # type: Tuple[int, str, float]

# ("Text" means  "unicode" in Python 2 and "str" in Python 3)
ListOfTextV = [u"one", u"two"]  # type: List[Text]

# Use Optional[] for values that could be None
# 标注可能值,下面只能OptionalStrV为None或者str
def some_function():
    return ''

OptionalStrV = some_function()  # type: Optional[str]

```

#### 验证测试（用例见test_built_in.py）

- **++只要赋值，不需要手动标注，就可以自动推导标注++**
```python
intV2 = 1                   #自动标注
intV2 = ''                  #报错，因为已经自动标注了
intV2 = ''  # type: str     #报错依旧
```

- 类型之间存在兼容，兼容不双向，int类型兼容bool，float类型兼容bool跟int
```python
intV = True                 #不报错
floatV = True               #不报错
floatV = 1                  #不报错
```
- 所有类型一经标注就不能修改成其他不兼容类型，也不能重新标注
- 检查仅限于类型，对可能的语法错是不管的
- 对于collection类型，并不会对所有方法进行检查，例如dict的in操作就没检查，has_key方法就检查了，但是比较常用的方法应该都是检查了。
- tuple存在两种标注方法（如下），前面的是指只有一个int元素的tuple，后面才是由不定的int元素组成的tuple

```python
tupleV2 = (3, ) # type: Tuple[int]
tupleV3 = (1, 2) # type: Tuple[int, ...]
```


### Funtions
#### 使用方法

```python
from typing import Callable, Iterable, Union, Optional, List

# 标注函数,标注另起一行
def stringify(num):
    # type: (int) -> str
    return str(num)

# 标注函数在同一行
def greet_world(): # type: () -> None
    print "Hello, world!"

# 多参数标注
def plus(num1, num2):
    # type: (int, int) -> int
    return num1 + num2

# 带default标注
def default(num1, my_float=3.5):
    # type: (int, float) -> float
    return num1 + my_float

# 标注禁止指定参数名的调用方式
def quux(__x):
    # type: (int) -> None
    pass

quux(3)  # Fine
quux(__x=3)  # Error

x = default  # type: Callable[[int, float], float]

# 标注yield生成器
def fIter(n):
    # type: (int) -> Iterable[int]
    i = 0
    while i < n:
        yield i
        i += 1
        
# 对每个参数单独打标注，然后在对函数的标注上忽略参数
def send_email(address,     # type: Union[str, List[str]]
               sender,      # type: str
               cc,          # type: Optional[List[str]]
               bcc,         # type: Optional[List[str]]
               subject='',
               body=None    # type: List[str]
               ):
    # type: (...) -> bool
    return True
```
#### 验证测试（用例见test_function.py）

- function的标注里，返回时用pass能适配int的报警，不知道是BUG还是特性。
- function的返回值标注可以帮助其他变量初始化
- 如果function本身没有被标注，那么其代码段的代码既不会被成功标注，也不会被检查

```python
def retFuncIntPass():
    # type: () -> int
    pass
    
intV = retFuncIntPass()
intV = ''       #Incompatible types in assignment (expression has type "str", variable has type "int")

```
### complicated情况

#### 使用方法

```python
from typing import Union, Any, List, Optional, cast

# 提示类型
reveal_type(1.0) # -> Revealed type is 'builtins.int'

# Union标注类型跟List混合，Union标注类型可以是可选中的一个
ListUionV = [3, 5, "test", "fun"]  # type: List[Union[int, str]]

# Any可以表示任何
def mystery_function():
    return

AnyV = mystery_function()  # type: Any

# Optional兼容None
ListV = []  # type: List[str]
OptionV = None  # type: Optional[str]

# This makes each positional arg and each keyword arg a "str"
# 下列方法标注所有args跟kwargs的key都是str
def call(self, *args, **kwargs):
    # type: (Any, *str, **str) -> str
    request = self.make_request(*args, **kwargs)
    return self.do_api_query(request)

# Use a "type: ignore" comment to suppress errors on a given line,
# when your code confuses mypy or runs into an outright bug in mypy.
# Good practice is to comment every "ignore" with a bug link
# (in mypy, typeshed, or your own code) or an explanation of the issue.
# ignore出错时用
ignoreV = confusing_function() # type: ignore # https://github.com/python/mypy/issues/1167

# "cast" is a helper function that lets you override the inferred
# type of an expression. It's only for mypy -- there's no runtime check.
# cast传递类型
a = [4]
b = cast(List[int], a)  # Passes fine
c = cast(List[str], a)  # Passes fine (no runtime check)
reveal_type(c)  # -> Revealed type is 'builtins.list[builtins.str]'
print c  # -> [4]; the object is not cast

# If you want dynamic attributes on your class, have it override "__setattr__"
# or "__getattr__" in a stub or in your source code.
#
# "__setattr__" allows for dynamic assignment to names
# "__getattr__" allows for dynamic access to names
# 标注__setattr__/__getattr__
class TestSetAttr:
    # This will allow assignment to any A.x, if x is the same type as "value"
    # (use "value: Any" to allow arbitrary types)
    def __setattr__(self, name, value):
        # type: (str, int) -> None
        pass
```


#### 验证测试（用例见test_complicated.py）

- 对于class的__getitem__/__setitem__/__get__/__set__/__setattr__/__getattr__均可标注，其他的类似方法还没有尝试。
- reveal_type(obj)可以获取obj的类型，不仅被标注的obj可以，没有被标注的也可以反向推导
- 无法通过标注检查的用ignore标注
- Any标注任何类型（实际上就是不知道）
- cast可以赋值的同时标注，但是似乎这次赋值就不会检查
```python
castVB = cast(int, '')
```
- Union类型的列表里可以填多个
```python
UionV = 100 # type: Union[int, str, bool, float]
UionV = ''
UionV = True
UionV = 1.0
UionV = None        #报警
```
- Optional类型只能选一个（觉得跟Union[xx, None]没区别）

### duck types

#### 使用方法

```python
from typing import Mapping, MutableMapping, Sequence, Iterable, List, Set

# Use Iterable for generic iterables (anything usable in "for"),
# and Sequence where a sequence (supporting "len" and "__getitem__") is
# required
# 标注序列迭代器
def funcIter(iterable_of_ints):
    # type: (Iterable[int]) -> List[str]
    return [str(x) for x in iterable_of_ints]

funcIter(range(1, 3))

# Mapping describes a dict-like object (with "__getitem__") that we won't
# mutate, and MutableMapping one (with "__setitem__") that we might
# Mapping标注不可修改的map型迭代器
def funcMap(my_dict):
    # type: (Mapping[int, str]) -> List[int]
    return list(my_dict.keys())

funcMap({3: 'yes', 4: 'no'})

# MutableMapping标注可修改的map型迭代器
def funcMutaleMap(my_mapping):
    # type: (MutableMapping[int, str]) -> Set[str]
    my_mapping[5] = 'maybe'
    return set(my_mapping.values())

funcMutaleMap({3: 'yes', 4: 'no'})
```

#### 验证测试（用例见test_complicated.py）
暂无特殊的用法尝试

### Classes

#### 使用方法

```python
class MyClass(object):
    # For instance methods, omit type for "self"
    def my_method(self, num, str1):
        # type: (int, str) -> str
        return num * str1

    # The "__init__" method doesn't return anything, so it gets return
    # type "None" just like any other method that doesn't return anything
    def __init__(self):
        # type: () -> None
        pass

# User-defined classes are valid as types in annotations
x = MyClass()  # type: MyClass
```

#### 验证测试（用例见test_classes.py）
- method的返回值标注也具有传导性，跟普通函数一样
- 能够检查到class是否有某个函数
- 能够检查到class是否有某个成员属性，甚至拼写错误带来的没有成员属性，也会提示
- 跟独立的function类似，class的属性标注跟属性检查，建立在代码所在function被标注的基础上，也就是说如果class的某个成员函数如果没有被标注，那么它代码段里的标注将不会被认可，也不会对它代码段的代码进行检查
- class的属性的标注完全按照代码中出现的位置先后来确定，先出现的标注生效（包括赋值的自动标注）
- 如果class没有function对某个属性进行标注（包括赋值的自动标注），在class外的代码上也不能使用，当然更加不能在class外进行标注

### Miscellaneous

#### 使用方法

```python
import sys
import re
from typing import Match, AnyStr, IO

# "typing.Match" describes regex matches from the re module
x = re.match(r'[0-9]+', "15")  # type: Match[str]

# Use IO[] for functions that should accept or return any
# object that comes from an open() call (IO[] does not
# distinguish between reading, writing or other modes)
def get_sys_IO(mode='w'):
    # type: (str) -> IO[str]
    if mode == 'w':
        return sys.stdout
    elif mode == 'r':
        return sys.stdin
    else:
        return sys.stdout
```
#### 验证测试（用例见test_miscellaneous.py）

用的比较少，暂无扩展用法尝试


## 复杂用例设想

### 继承标注（测试用例见test_inherit.py）

- 首先依旧继承class跟function相关的标注跟检查规则、特性
- 如果派生类跟基类都对同名属性进行了标注，那么会在派生类标注处报警，但是后续派生类会使用新的标注（派生类打的）来进行检查
- 对于function的标注也类似属性，如果基类标注了，派生类再对同名函数打一次标注，那么会在标注处打一个告警，然后替换掉标注

### 修饰器标注（测试用例见test_decorator.py）

- 对修饰器的标记必须标注在修饰函数上，而不是标记在修饰器的生成函数上，并且没有对修饰器标注的情况下，修饰器会抹掉函数的标注信息。
```python
#不生效
def test_decoratorA(func):
    def newfunc(arg):
        # type: (str) -> None
        return

    return newfunc

#生效
def test_decoratorB(func):
    # type: (Callable) -> Callable[[str], None]
    def newfunc(arg):
        return

    return newfunc
    
@test_decoratorA
def testFuncA(arg):
    # type: (int) -> None
    return

@test_decoratorB
def testFuncB(arg):
    # type: (int) -> None
    return

testFuncA(None) #啥都不报
testFuncB(None) #报警
```
- 如果对修饰器进行了标记，同时对生成函数进行了标记，并且两个标记不一样，会检查报个错
- 

### 跨模块标注（测试用例见test_mod_1.py跟test_mod_2.py）

- 能完美检查出test_mod_1里定义但是test_mod_2使用的function、class、decorator
- 如果跨了目录进行import并且检查，那么可以选择对MYPYPATH进行修改，例如testfolder2/test_mod_2.py里import了testfolder1/test_mod_1.py
```shell
gzweikun@VM-23-26-debian:~/LearnTest/TestMyPy/testfolder2$ export MYPYPATH=~/LearnTest/TestMyPy/testfolder1:$MYPYPATH
gzweikun@VM-23-26-debian:~/LearnTest/TestMyPy/testfolder2$ mypy --py2 test_mod_2.py                                  
test_mod_2.py:9: error: Argument 1 to "functionA" has incompatible type "str"; expected "int"
test_mod_2.py:11: error: Argument 1 to "functionA" of "Base" has incompatible type "str"; expected "int"
test_mod_2.py:18: error: Argument 1 to "func" has incompatible type "str"; expected "int"
```

## 高级进阶用法
待补充

## 性能测试

小文件上能明显感觉到卡顿，但是没有大项目，所以无法验证具体性能指标

## 对大系统的使用想法
