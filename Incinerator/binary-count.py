# https://py.checkio.org/en/mission/binary-count/
# Difficulty : Elementary

def checkio(n):
    return bin(n).count("1")

# Example)
# checkio(4) == 1
# checkio(15) == 4
# checkio(1) == 1
# checkio(1022) == 9
