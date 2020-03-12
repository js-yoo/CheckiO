# https://py.checkio.org/en/mission/even-last/
# Difficulty : Elementary

def checkio(array):
    if len(array)!=0:
        summed=sum(array[::2])
        return summed*array[-1]
    else:
        return 0

# Example)
# checkio([0, 1, 2, 3, 4, 5]) == 30
# checkio([1, 3, 5]) == 30
# checkio([6]) == 36
# checkio([]) == 0
