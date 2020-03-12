# https://py.checkio.org/en/mission/fizz-buzz/
# Difficulty : Elementary

def checkio(num:int)->str:
    if num%15==0:
        return ("Fizz Buzz")
    elif num%3==0:
        return ("Fizz")
    elif num%5==0:
        return ("Buzz")
    else:
        return str(num)

# Example)
# checkio(15) == "Fizz Buzz"
# checkio(6) == "Fizz"
# checkio(5) == "Buzz"
# checkio(7) == "7"
