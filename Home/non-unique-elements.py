# https://py.checkio.org/en/mission/non-unique-elements/
# Difficulty : Elementary

def checkio(data:list):
    ans=[]
    for a in data:
        if data.count(a)>1:
            ans.append(a)
    return ans

# Example)
# checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3]
# checkio([1, 2, 3, 4, 5]) == []
# checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
# checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]
