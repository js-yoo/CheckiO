# https://py.checkio.org/en/mission/first-word-simplified/
# Difficulty : Elementary

def first_word(text:str)->str:
    ans=''
    for a in text:
        if a.isalpha():
            ans+=a
        else:
            return ans
    return ans

# Example)
# first_word("Hello world") == "Hello"
