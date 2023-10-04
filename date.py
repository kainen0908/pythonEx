# 날짜/시간과 관련된 기능 호출
import datetime

# 현재
now = datetime.datetime.now()

# 출력
print(now.year,"년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute,"분")
print(now.second,"초")

print("{}년 {}월 {}일 {}시 {}분 {}초".format(
      now.year,
      now.month,
      now.day,
      now.hour,
      now.minute,
      now.second
))

if 3 <= now.month <= 5:
  print("이번 달은 {}월로 봄입니다.".format(now.month))
elif now.month <= 8:
  print("이번 달은 {}월로 여름입니다.".format(now.month))
elif now.month <= 11:
  print("이번 달은 {}월로 가을입니다.".format(now.month))
else:
  print("이번 달은 {}월로 겨울입니다.".format(now.month))      