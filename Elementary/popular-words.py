# https://py.checkio.org/en/mission/popular-words/
# Difficulty : Elementary

def popular_words(text:str,array:list):
    text=text.lower().split()
    answer={}
    for a in array:
        answer[a]=text.count(a)
    return answer

# Example)
# popular_words('''
# When I was One
# I had just begun
# When I was Two
# I was nearly new
# ''', ['i', 'was', 'three', 'near']) == {
#     'i': 4,
#     'was': 3,
#     'three': 0,
#     'near': 0
# }
