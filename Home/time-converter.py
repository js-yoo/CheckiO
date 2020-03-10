# https://py.checkio.org/en/mission/time-converter-24h-to-12h/
# Difficulty : Elementary

def time_converter(time):
    h,m=map(int,time.split(':'))
    if h<12:
        ampm='a.m.'
    else:
        ampm='p.m.'
    
    if h>12:
        h-=12
    elif h==0:
        h=12
    
    return '%d:%02d %s' % (h,m,ampm)

# Example)
# time_converter('12:30') == '12:30 p.m.'
# time_converter('09:00') == '9:00 a.m.'
# time_converter('23:15') == '11:15 p.m.'
