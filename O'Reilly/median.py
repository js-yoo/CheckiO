# https://py.checkio.org/en/mission/median/
# Difficulty : Elementary

from typing import List

def checkio(data:List[int])->[int,float]:
    a=sorted(data)
    b=len(data)
    if b%2==0:
        return (a[int(b/2)-1]+a[int(b/2)])/2
    else:
        return (a[int(b/2)])

# Example0
# checkio([1, 2, 3, 4, 5]) == 3
# checkio([3, 1, 2, 5, 3]) == 3
# checkio([1, 300, 2, 200, 1]) == 2
# checkio([3, 6, 20, 99, 10, 15]) == 12.5
