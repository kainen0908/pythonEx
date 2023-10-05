numbers=[273, 103, 5, 32, 65, 9, 72, 800, 99]

for i in numbers:
  print(i, "는", len(str(i)), "자릿수입니다.")
print()

for i in numbers:
  cnt = 1
  j = i
  while i/10**cnt >= 1:
    j = i/10**cnt
    cnt += 1
  print(i, "는", cnt, "자릿수입니다.")