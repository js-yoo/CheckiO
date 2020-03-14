# https://py.checkio.org/en/mission/absolute-sorting/
# Difficulty : Elementary

def checkio(array:tuple)->list:
    return sorted(array,key=abs)

# Example) 
# checkio((-20, -5, 10, 15)) == [-5, 10, 15, -20] # or (-5, 10, 15, -20)
# checkio((1, 2, 3, 0)) == [0, 1, 2, 3]
# checkio((-1, -2, -3, 0)) == [0, -1, -2, -3]
