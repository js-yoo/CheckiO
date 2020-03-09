# https://py.checkio.org/en/mission/all-the-same/
# Difficulty : Elementary

from typing import List, Any

def all_the_same(data:List[Any])->bool:
    return len(set(data)) <=1


# Example)
# all_the_same([1, 1, 1]) == True
# all_the_same([1, 2, 1]) == False
# all_the_same(['a', 'a', 'a']) == True
# all_the_same([]) == True
