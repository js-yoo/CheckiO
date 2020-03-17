# https://py.checkio.org/en/mission/count-consecutive-summers/
# Difficulty : Elementary

def count_consecutive_summers(num:int):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    
    if num%2==0: # 짝수
        return round(count/3)
    else:
        return count

# Example)
# count_consecutive_summers(42) == 4
# count_consecutive_summers(99) == 6
