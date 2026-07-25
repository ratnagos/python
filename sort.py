sort = [2,23,45,453,67]
print(sort)

t = [2,23,45,453,67]  #Sort the list in place
t=t.sort()
print(t)

t = ['a', 'b', 'c']   #Delete the last element of the list
x = t.pop(2)
print(t)

t = ['a', 'b', 'c', 'g', 'h','i', 'j']  #remove the last element of the list
t.remove('b')
print(t)

t = ['a', 'b', 'c', 'd', 'e', 'f', 'h', 'i']  #delete the last element of the list
del t[1:5]
print(t)
