# https://py.checkio.org/en/mission/first-word/
# Difficulty : Elementary

def first_word(text:str)->str:
    text=text.replace(',',' ').replace('.',' ')
    text=text.lstrip().rstrip()
    ans=''
    for a in text:
        if not a.isspace():
            ans+=a
        else:
            return ans
    return ans

# Example)
# first_word("Hello world") == "Hello"
# first_word("greetings, friends") == "greetings"
