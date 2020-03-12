# https://py.checkio.org/en/mission/right-to-left/
# Difficulty : Elementary

def left_join(text:tuple)->str:
    join_text=",".join(text)
    result=join_text.replace("right","left")
    return result

# Example)
# left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
# left_join(("bright aright", "ok")) == "bleft aleft,ok"
# left_join(("brightness wright",)) == "bleftness wleft"
# left_join(("enough", "jokes")) == "enough,jokes"
