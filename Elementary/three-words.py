# https://py.checkio.org/en/mission/three-words/
# Difficulty: Elementary

def checkio(text:str)->bool:
    count=0
    for a in text.split():
        if a.isalpha():
            count+=1
            if count >=3:
                break
        else:
            count=0
    return count>=3

# Example)
# checkio("Hello World hello") == True
# checkio("He is 123 man") == False
# checkio("1 2 3 4") == False
# checkio("bla bla bla bla") == True
# checkio("Hi") == False
