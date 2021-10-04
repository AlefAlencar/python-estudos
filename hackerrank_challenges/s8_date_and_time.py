"""
DESAFIOS HACKERRANK

08. Date and Time
"""

import calendar

# Exemplos
'''print(calendar.TextCalendar(firstweekday=6).formatyear(2021))
# '''

# 1/2 Calendar Module (easy)
'''data = list(map(int, input().split()))
d = calendar.weekday(data[2], data[0], data[1])
wd = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
print(d)
print(wd[d])  # '''

# 2/2 Time Delta (easy)
'''# Day dd Mon yyyy hh:mm:ss +xxxx
from datetime import datetime
fmt = '%a %d %b %Y %H:%M:%S %z'
for _ in range(int(input())):  # INPUT
    t1, t2 = input(), input()
    print(int(abs((datetime.strptime(t1, fmt) - datetime.strptime(t2, fmt)).total_seconds())))  # PROCESS, OUTPUT
# '''
