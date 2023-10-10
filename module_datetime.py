# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:21:48 2023

@author: kainen
"""

import datetime

now = datetime.datetime.now()

after = now+datetime.timedelta(weeks=1, days=1, hours=1, minutes=1, seconds=1)

# print(now.year, "년")
# print(now.month, '월')
# print(now.day, '일')
# print(now.hour, '시')
# print(now.minute, '분')
# print(now.second, '초')
# print()

# output_a = now.strftime('%Y.%m.%d %H:%M:%S')
# output_b = '{}년 {}월 {}일 {}시 {}분 {}초'.format(now.year,\
#                                              now.month, now.day, now.hour, now.minute, now.second)

# output_c = now.strftime('%Y{} %m{} %d{} %H{} %M{} %S{}').format(*'년월일시분초')
# print(output_a)
# print(output_b)
# print(output_c)

print(after.strftime('%Y{} %m{} %d{} %H{} %M{} %S{}').format(*'년월일시분초'))
print()

output = now. replace(year=(now.year+1))
print(output.strftime('%Y{} %m{} %d{} %H{} %M{} %S{}').format(*'년월일시분초'))
