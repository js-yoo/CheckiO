# https://py.checkio.org/en/mission/sun-angle/
# Difficulty : Elementary

def sun_angle(time):
  h,m=map(int,time.split(':'))
  dtime=60*h+m-360
  if -1<dtime<721:
    return dtime/4
  else:
    return "I don't see the sun!"

# Example)
# sun_angle("07:00") == 15
# sun_angle("12:15"] == 93.75
# sun_angle("01:23") == "I don't see the sun!"
