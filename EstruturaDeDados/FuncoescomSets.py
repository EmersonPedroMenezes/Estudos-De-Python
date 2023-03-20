list1 = set([1, 2, 3, 4, 5, 6, 1, 2])
s1= {1, 2, 3, 4, 5, 6}
#s1.add(7)
s1.update([7, 8, 9, 10])
s1.remove(10)
s1.discard(9)

print(type(list1))
print(s1)
print(type(s1))

