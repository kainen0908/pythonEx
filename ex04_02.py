numbers=[1,2,3,4,5,6,7,8,9]
output = [[],[],[]]

for number in numbers:
  output[number%3-1].append(number)
print (output)