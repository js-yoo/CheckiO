# https://py.checkio.org/en/mission/easy-unpack/
# Difficulty : Elementary

def easy_unpack(elements: tuple) -> tuple:
    return elements[0],elements[2],elements[-2]

# Example)
# easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
# easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
# easy_unpack((6, 3, 7)) == (6, 7, 3)
