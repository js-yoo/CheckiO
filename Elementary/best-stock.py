# https://py.checkio.org/en/mission/best-stock/
# Difficulty : Elementary

def best_stock(text)->str:
    max_price=0
    answer=''
    for a in text:
        if text[a]>max_price:
            max_price=text[a]
            answer=a
    return answer

# Example)
# best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}) == "ATX"
# best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}) == "TASI"
