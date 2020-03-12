# https://py.checkio.org/en/mission/correct-sentence/
# Difficulty : Elementary

def correct_sentence(text:str)->str:
    if text[-1]=="." and text[0].isupper():
        return text
    else:
        if not text[0].isupper():
            text=text[0].upper()+text[1:]+"."
            return text
        else:
            return text+"."   

# Example)
# correct_sentence("greetings, friends") == "Greetings, friends."
# correct_sentence("Greetings, friends") == "Greetings, friends."
# correct_sentence("Greetings, friends.") == "Greetings, friends."
