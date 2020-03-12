# https://py.checkio.org/en/mission/secret-message/
# Difficulty : Elementary

def find_message(text: str) -> str:
    return "".join([ch for ch in text if ch.isupper()])

# Example)
# find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO"
# find_message("hello world!") == ""
