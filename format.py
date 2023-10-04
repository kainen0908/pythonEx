# format
format_a = "{}만 원".format(5000)
format_b = "파이썬 열공하여 첫 연봉 {}만 원 만들기".format(5000)
format_c = "{} {}".format(10,20)
format_d = "{} + {} = {}".format(10, 20, 10+20)
format_e = "{}  {} {}".format(1, "문자열", True)
print(format_a)
print(format_b)
print(format_c)
print(format_d)
print(format_e)

#정수
output_a = "{:d}".format(52)
output_a1 = "{:o}".format(52)
output_a2 = "{:x}".format(52)


# 특정 칸에 출력하기
output_b = "{:5d}".format(52)
output_c = "{:10d}".format(52)

# 빈칸 0 채우기
output_d = "{:05d}".format(52)
output_e = "{:05d}".format(-52)

# 기호와 함께 출력
output_f = "{:+d}".format(52)
output_g = "{:+d}".format(-52)
output_h = "{: d}".format(52)
output_i = "{: d}".format(-52)


print(output_a)
print(output_a1)
print(output_a2)
print(output_b)
print(output_c)
print(output_d)
print(output_e)
print(output_f)
print(output_g)
print(output_h)
print(output_i)