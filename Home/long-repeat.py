# https://py.checkio.org/en/mission/long-repeat/
# Difficulty : Simple

def long_repeat(line):
    counter, max_counter = 0,0
    text = line.lower()
    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            counter += 1
        else:
            max_counter = max(max_counter, counter+1)
            counter = 0
    return len(text) and max(max_counter, counter+1)

# Example)
# long_repeat('sdsffffse') == 4
# long_repeat('ddvvrwwwrggg') == 3
