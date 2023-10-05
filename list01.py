list_a = [1,2,3]
list_b = [4,5,6]

print("list_a = ", list_a)
print("list_b = ", list_b)
print()

print("list_a + list_b = " , list_a+list_b)
print("list_a * 3 = ", list_a * 3)
# list_a + list_b =  [1, 2, 3, 4, 5, 6]
# list_a * 3 =  [1, 2, 3, 1, 2, 3, 1, 2, 3]
print()

print("len(list_a) = ", len(list_a))
# len(list_a) =  3

list_a.extend([4,5,6])
print(list_a)

list_a.append(4)
list_a.append(5)
print(list_a)
# [1, 2, 3, 4, 5]
print()

list_a.insert(0, 10)
# [10, 1, 2, 3, 4, 5]
print(list_a)

# >>> list1=[1,2,3]
# >>> list2=[4,5,6]
# >>> list1+list2
# [1, 2, 3, 4, 5, 6]
# >>> list1
# [1, 2, 3]
# >>> del list1[1]
# >>> list1
# [1, 3]
# >>> a = list1.pop()
# >>> a
# 3
# >>> list1
# [1]
# >>> list_b=[0,1,2,3,4,5,6]
# >>> del list_b[3:6]
# >>> list_b
# [0, 1, 2, 6]
# >>> list_c=[0,1,2,3,4,5,6]
# >>> del list_c[:3]
# >>> list_c
# [3, 4, 5, 6]
# >>> del list_c[2:]
# >>> list_c
# [3, 4]