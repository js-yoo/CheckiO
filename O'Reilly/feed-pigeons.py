# https://py.checkio.org/en/mission/feed-pigeons/
# Difficulty : Simple

def checkio(portions):
    fed = minute = pigeons = 0
    while portions >= 0:
        portions -= pigeons
        minute += 1
        print(minute)
        if portions <= 0:
            return fed
        if minute < portions:
            fed += minute
            portions -= minute
        else:
            fed += portions
            return fed
        pigeons += minute
    return fed

# Example)
# checkio(1) == 1
# checkio(2) == 1
# checkio(5) == 3
# checkio(10) == 6
