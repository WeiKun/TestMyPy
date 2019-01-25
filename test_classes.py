# -*- coding: utf-8 -*-
from typing import Any
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

    def add(self):
        # type: () -> None
        return
	
    def sub(self):
        # type: () -> None
        self.Hello = None   #会默认标注成None
        self.Any = None # type: Any
        return
	

# User-defined classes are valid as types in annotations
classV = MyClass()  # type: MyClass


#test
strV = classV.my_method(1, 1)    #报错
strV = 1                         #报错,上面的错误调用并不影响推导标注

intV = classV.Hello()           #报错
classV.Hello = 1                #报错
classV.Any = 1                  #不报错,因为Any
print classV.hello              #报错，而且奇妙的是能提示是不是敲错了#"MyClass" has no attribute "hello"; maybe "Hello"?
classV.TestA = 10               #报错，因为MyClass没有这个属性
classV.TestB = 10               # type: Any  #也会报错,不能在class外进行赋值


class MyClassB(object):
    ATTRA = 10                  #自动标注
    def funcA(self):
        # type: () -> None
        self.ATTRA = ''         #报警，因为class已经有ATTRA的类型标注int
        self.attrA = ''         #自动标注
        return

    def __init__(self):
        # type: () -> None
        self.ATTRA = None       #报警
        self.attrA = None       #报警，attrA由先出现的funcA自动标注，而不会对__init__另眼相看
    

classVB = MyClassB()
classVB.ATTRA = [] #Incompatible types in assignment (expression has type "List[<nothing>]", variable has type "int")
classVB.attrA = [] #Incompatible types in assignment (expression has type "List[<nothing>]", variable has type "str")


