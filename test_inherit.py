# -*- coding: utf-8 -*-
class Base(object):
    def __init__(self):
        # type: () -> None
        self.vA = 1 # type: int
        self.vB = 1 # type: int

    def setFuncA(self, arg):
        # type: (int) -> None
        self.vA = '' # type: str    #报错，跟__init__里的冲突

    def setFuncB(self, arg):
        # type: (int) -> None
        self.vA = ''                #报错，跟__init__里的冲突
        self.vB = ''                 #报错，跟__init__里的冲突
    

class DerivedA(Base):
    def __init__(self):
        # type: () -> None
        self.vA = None # type: None  #报错，跟base冲突
        self.vB = ''                 #报错

    def setFuncA(self, arg):
        # type: (str) -> None   #跟base冲突#Argument 1 of "setFuncA" incompatible with supertype "Base"
        self.vA = [] # type: list  #跟自己的标注冲突#Incompatible types in assignment (expression has type"List[<nothing>]", variable has type "None")

    def setFuncC(self):
        # type: () -> None
        self.setFuncA('')
        self.setFuncB('')           
        return

class DerivedB(Base):
    pass

testVA = DerivedA()
testVA.vA = {}          #用的派生类的标注做的检查#Incompatible types in assignment (expression has type "Dict[<nothing>,<nothing>]", variable has type "None")
testVA.setFuncA(1)      #用的派生类的标注做的检查#Argument 1 to "setFuncA" of "DerivedA" has incompatible type "int"; expected "str"
testVA.setFuncA('')
testVA.setFuncB('')     #报错,用基类的检查

#DerivedB的检查沿用基类，不表
testVB = DerivedB()
testVB.vA = None        #报错
testVB.vA = ''          #报错
testVB.vB = ''          #报错
testVB.setFuncA(1)
testVB.setFuncA('')     #报错
testVB.setFuncB('')     #报错
