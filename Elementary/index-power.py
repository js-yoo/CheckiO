# https://py.checkio.org/en/mission/index-power/
# Difficulty : Elementary

def index_power(array: list, n: int) -> int:
    if n<len(array):
        return array[n]**n
    else:
        return -1

# Example)
# index_power([1, 2, 3, 4], 2) == 9
# index_power([1, 3, 10, 100], 3) == 1000000
# index_power([0, 1], 0) == 1
# index_power([1, 2], 3) == -1
