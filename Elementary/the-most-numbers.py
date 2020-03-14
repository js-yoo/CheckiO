# https://py.checkio.org/en/mission/most-numbers/
# Difficulty : Elementary

def checkio(*args):
    return (max(args)-min(args)) if len(args)>0 else 0

# Example)
# checkio(1, 2, 3) == 2
# checkio(5, -5) == 10
# checkio(10.2, -2.2, 0, 1.1, 0.5) == 12.4
# checkio() == 0
