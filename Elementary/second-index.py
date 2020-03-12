# https://py.checkio.org/en/mission/second-index/
# Difficulty : Elementary

def second_index(sen:str,symbol:str)->[int,None]:
    if sen.count(symbol)<2:
        return None
    else: 
        first=sen.find(symbol)
        return sen.find(symbol,first+1)

# Example)
# second_index("sims", "s") == 3
# second_index("find the river", "e") == 12
# second_index("hi", " ") is None
