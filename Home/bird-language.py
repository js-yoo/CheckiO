# https://py.checkio.org/en/mission/bird-language/
# Difficulty : Elementary

VOWELS="aeiouy"

def translate(phrase):
  
  for c in VOWELS:
    phrase=phrase.replace(c*3,c)
  
  phrase=list(phrase)

  for i,c in enumerate(phrase):
    if c not in VOWELS and c !=' ':
      del phrase[i+1]

  return ''.join(phrase)

# Example)
# translate("hieeelalaooo") == "hello"
# translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
# translate("aaa bo cy da eee fe") == "a b c d e f"
# translate("sooooso aaaaaaaaa") == "sos aaa"
