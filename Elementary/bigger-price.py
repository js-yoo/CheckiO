# https://py.checkio.org/en/mission/bigger-price/
# Difficulty : Elementary

def bigger_price(limit, data):
    return sorted(data, key=lambda x: x['price'],reverse=True)[:limit]

# Example)
# bigger_price(2, [
#     {"name": "bread", "price": 100},
#     {"name": "wine", "price": 138},
#     {"name": "meat", "price": 15},
#     {"name": "water", "price": 1}
# ]) == [
#     {"name": "wine", "price": 138},
#     {"name": "bread", "price": 100}
# ]
#
# bigger_price(1, [
#     {"name": "pen", "price": 5},
#     {"name": "whiteboard", "price": 170}
# ]) == [{"name": "whiteboard", "price": 170}]
