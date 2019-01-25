# -*- coding: utf-8 -*-
from typing import Mapping, MutableMapping, Sequence, Iterable, List, Set

# Use Iterable for generic iterables (anything usable in "for"),
# and Sequence where a sequence (supporting "len" and "__getitem__") is
# required
def funcIter(iterable_of_ints):
    # type: (Iterable[int]) -> List[str]
    return [str(x) for x in iterable_of_ints]

funcIter(range(1, 3))

# Mapping describes a dict-like object (with "__getitem__") that we won't
# mutate, and MutableMapping one (with "__setitem__") that we might
def funcMap(my_dict):
    # type: (Mapping[int, str]) -> List[int]
    return list(my_dict.keys())

funcMap({3: 'yes', 4: 'no'})

def funcMutaleMap(my_mapping):
    # type: (MutableMapping[int, str]) -> Set[int]
    my_mapping[5] = 'maybe'
    return set(my_mapping.keys())

funcMutaleMap({3: 'yes', 4: 'no'})

#test
funcIter(xrange(3))
def funcMapB(my_dict):
    # type: (Mapping[int, str]) -> List[int]
    my_dict[1] = ''                     #报错 Mapping只读不可写
    return list(my_dict.keys())
funcMapB({3: 'yes', 4: 'no'})




