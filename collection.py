mylist=[1,235,34,54,356,364,43,43,356]

print(mylist)
print(mylist[1:3])
print(mylist[0:3])
print(mylist[3:])
print(mylist[::])
print(mylist[1:6:2])
print(mylist[1::2])
print(mylist[9::-1])
print(mylist[9:5:-1])
mylist.sort()
print(mylist)
mylist.sort(reverse=True)
print(mylist)
mylist.insert(4,10000)
print(mylist)
mylist.remove(34)
print(mylist)
mylist.extend([43,35,3636,364])
print(mylist)