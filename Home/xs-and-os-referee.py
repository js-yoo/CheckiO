# https://py.checkio.org/en/mission/x-o-referee/
# Difficulty : Simple

def checkio(code:list):
    sample="".join(code)
    data=code+[sample[i:9:3] for i in range(3)]+[sample[2:7:2]]+[sample[0:9:4]]
    if 'XXX' in data:
        return "X"
    elif 'OOO' in data:
        return "O"
    else:
        return "D"

# Example)
# checkio([
#   "X.O",
#   "XX.",
#   "XOO"]) == "X"
# checkio([
#    "OO.",
#   "XOX",
#   "XOX"]) == "O"
# checkio([
#   "OOX",
#    "XXO",
#    "OXX"]) == "D"
