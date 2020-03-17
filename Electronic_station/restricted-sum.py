# https://py.checkio.org/en/mission/restricted-sum/
# Difficulty : Elementary

def checkio(number:list):
    return number.pop()+checkio(number) if number else 0

# Example)
# checkio([1, 2, 3]) == 6
# checkio([2, 2, 2, 2, 2, 2]) == 12
