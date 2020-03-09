# https://py.checkio.org/en/mission/all-the-same/

from typing import List, Any

def all_the_same(data:List[Any])->bool:
    return len(set(data)) <=1
