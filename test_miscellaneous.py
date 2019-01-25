# -*- coding: utf-8 -*-
import sys
import re
from typing import Match, AnyStr, IO, Optional

# "typing.Match" describes regex matches from the re module
x = re.match(r'[0-9]+', "15")  # type: Optional[Match[str]]

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

