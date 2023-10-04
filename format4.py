output_a = "{:15.3f}".format(52.273)
output_b = "{:15.2f}".format(52.273)
output_c = "{:15.1f}".format(52.273)

# 의미없는 소수점 제거
output_d = "{:g}".format(52.1)
output_e = "{:.0f}".format(52.1)


print(output_a)
print(output_b)
print(output_c)
print(output_d)
print(output_e)