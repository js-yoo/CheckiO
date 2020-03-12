# https://py.checkio.org/en/mission/digits-multiplication/
# Difficulty : Elementary

def checkio(number: int) -> int:
    result=1
    for s in str(number):
        n=int(s)
        if not n:
            continue
        result=result*n
    return result    

# Example)
# checkio(123405) == 120
# checkio(999) == 729
# checkio(1000) == 1
# checkio(1111) == 1
