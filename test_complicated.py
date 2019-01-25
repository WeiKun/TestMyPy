# -*- coding: utf-8 -*-
from typing import Union, Any, List, Optional, cast

# To find out what type mypy infers for an expression anywhere in
# your program, wrap it in reveal_type().  Mypy will print an error
# message with the type; remove it again before running the code.
# 提示类型
reveal_type(1.0) # -> Revealed type is 'builtins.int'

# Use Union when something could be one of a few types
# Union标记类型跟List混合，Union标记类型可以是可选中的一个
ListUionV = [3, 5, "test", "fun"]  # type: List[Union[int, str]]

# Use Any if you don't know the type of something or it's too
# dynamic to write a type for

def mystery_function():
    return

AnyV = mystery_function()  # type: Any

# If you initialize a variable with an empty container or "None"
# you may have to help mypy a bit by providing a type annotation
ListV = []  # type: List[str]
OptionV = None  # type: Optional[str]

# This makes each positional arg and each keyword arg a "str"
def call(self, *args, **kwargs):
    # type: (Any, *str, **str) -> str
    request = self.make_request(*args, **kwargs)
    return self.do_api_query(request)

# Use a "type: ignore" comment to suppress errors on a given line,
# when your code confuses mypy or runs into an outright bug in mypy.
# Good practice is to comment every "ignore" with a bug link
# (in mypy, typeshed, or your own code) or an explanation of the issue.
ignoreV = confusing_function() # type: ignore # https://github.com/python/mypy/issues/1167

# "cast" is a helper function that lets you override the inferred
# type of an expression. It's only for mypy -- there's no runtime check.
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
class TestSetAttr:
    # This will allow assignment to any A.x, if x is the same type as "value"
    # (use "value: Any" to allow arbitrary types)
    def __setattr__(self, name, value):
        # type: (str, int) -> None
        pass

SetAttrV = TestSetAttr()
SetAttrV.foo = 42  # Works
SetAttrV.bar = 'Ex-parrot'  # Fails type checking

#test 验证测试
#测试SetItem
class TestSetItem(object):
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        # type: (str) -> int
        return self.data.get(key, None)

    def __setitem__(self, key, value):
        # type: (str, int) -> None
        self.data[key] = value
        pass

SetItemV = TestSetItem()
SetItemV['1'] = 1
SetItemV[1] = 1             #报错，触犯了对__setitem__的标注
_ = SetItemV[1]             #报错，触犯了对__getitem__的标注

#测试Set
class TestSet(object):
    def __init__(self, value):
        self.value = value

    def __get__(self, obj, objtype):
        # type: (Any, Any) -> int
        return self.value

    def __set__(self, obj, val):
        # type: (Any, int) -> None
        self.value = val
        return

class TestSet2(object):
    x = TestSet(10)
    y = TestSet('20')

TestSetV = TestSet2()
TestSetV.x = '10'               #报错，触犯对__set__的检查
_ = TestSetV.x + ''             #报错，触犯对__get__的检查
print TestSetV.y

def func():
    return 10
revealV = func()
reveal_type(revealV)    #类型推导

castVA = cast(int, 10)  
castVA = ''             #报警
castVB = cast(int, '')  #不报警
castVB = ''             #报警

UionV = 100 # type: Union[int, str, bool, float]
UionV = ''
UionV = True
UionV = 1.0
UionV = None        #报警

OptionVB = '' # type: Optional[int, str]

UionVB = None # type: Union[int, None]

