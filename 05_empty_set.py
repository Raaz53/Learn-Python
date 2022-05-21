# Important this will create an empty dictionary not an empty set
# a = {}
# print(a)
#  an empty set can be made by using following syntax:
b = set()
print(type(b))
# adding values to an empty set
b.add(2)
b.add(4)
b.add(2)
b.add(5) # adding a value repetedly does not change the value
b.add((1, 5, 9)) # list cannot be added
print(b)
print(len(b))
b.remove(5)
print(b)