# -*- coding: utf-8 -*-
from typing import List, Set, Dict, Tuple, Text, Optional

# For simple built-in types, just use the name of the type
# 标记基础类型
intV = 1  # type: int
floatV = 1.0  # type: float
boolV = True  # type: bool
strV = "test"  # type: str
unicodeV = u"test"  # type: unicode
noneV = None    # type: None

# For collections, the name of the type is capitalized, and the
# name of the type inside the collection is in brackets
# 标记list/set
listV = [1]  # type: List[int]
setV = {6, 7}  # type: Set[int]

# For mappings, we need the types of both keys and values
# 标记dict,可以指定key/value类型
dictV = {'field': 2.0}  # type: Dict[str, float]

# For tuples, we specify the types of all the elements
# 标记tuple
tupleV = (3, "yes", 7.5)  # type: Tuple[int, str, float]
tupleV2 = (3, ) # type: Tuple[int]

# For textual data, use Text
# ("Text" means  "unicode" in Python 2 and "str" in Python 3)
ListOfTextV = [u"one", u"two"]  # type: List[Text]

# Use Optional[] for values that could be None
def some_function():
    return ''

# 标记可能值,下面只能OptionalStrV为None或者str
OptionalStrV = some_function()  # type: Optional[str]

# Mypy understands a value can't be None in an if-statement
# 还不明白
if OptionalStrV is not None:
    print OptionalStrV.upper()

# If a value can never be None due to some invariants, use an assert
# 还不明白
assert OptionalStrV is not None
print OptionalStrV.upper()

#test code 验证测试
#基础数据类型如果符合兼容性要求，就可以通过检查，例如给int标注的变量赋值bool
intV = ''                   #报错
intV = True                 #不报错
intV = 1.0                  #报错
intV = None                 #报错

floatV = ''                 #报错
floatV = True               #不报错
floatV = 1                  #不报错
floatV = None               #报错

boolV = ''                  #报错
boolV = 1                   #报错
boolV = 1.0                 #报错
boolV = None                #报错

strV = 1                    #报错

unicodeV = 1                #报错

noneV = 1                   #报错

#重新标注报错
noneV = 1   # type: int

#listV被标注成List[int]，因此对于append其他类型，会报错
listV.append('')            #报错 
listV[0] = 1                #不报错
listV[2] = 3                #不报错
listV[3] = ''               #报错
listV = ''                  #报错
listV = tupleV2             #报错

#setV标注是Set[int]
print ('' in setV)          #不报错
setV.add('')                #报错 
setV.remove('')             #报错 

#dictV标注的是Dict[str, float]
print (1 in dictV)          #不报错
print dictV.has_key(1)      #报错
print dictV.get(1, None)    #报错
print dictV.get(1, 2.0)     #报错
print dictV.get('', None)   #不报错
print dictV.get('', 2.0)    #不报错
dictV[1] = 1                #报错
dictv.pop(1)                #报错

#tupleV标注类型是Tuple[int, str, float],所以[1]是str
print tupleV[1] + 1         #报错
tupleV = (1, 2)             #报错
tupleV = (2, '', 0.1)       #不报错
#tupleV2标注类型Tuple[int]
tupleV2 = listV             #报错
tupleV2 = (1, 2)            #报错
#这种才是int组成并且数量不定的tuple
tupleV3 = (1, 2) # type: Tuple[int, ...]
tupleV3 = (1, 2, 3)         #不报错

OptionalStrV = 1            #报错
print OptionalStrV.upper()  #不报错

#！！！！！最重要的，赋值可以自动标注！！！！！！！
intV2 = 1                   #自动标注
intV2 = ''                  #报错，因为已经自动标注了
intV2 = ''  # type: str     #报错依旧

