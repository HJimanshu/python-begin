a={1,2,3,5,4}#set is denoted by curley phrases{}
print(type(a))#type casting
print(a)
a={4,2,54,6,1,8,0}
print(a)#it is never follow thw sequence of set literals
# print(a[3])#set litrals cannot be fetching using indexing
b={1,2,34,2,21,4,5,6,733,5,78,5,9,7,6,6}
print(b)#set does not permit duplicate values
#using some method are used in set{}
c={1,2,3,4,5,6,}
d={3,5,6,3,9,8,7,6}
print(c|d)#these are the way to union between twi sets
print(c.union(d))#using union method to return a  unique set.
print(c&d)#these are the way to intersection between two sets
print(d.intersection(c))#using intersection method to return the set that contain the similarity between two and more sets.
print(c-d)
print(d-c)#these are the way to difference between two sets
print(c.difference(d))#using difference method to return the set that contain the difference between two sets
print(len(a))#using len () method for length of set
a.add(30)#we should be add a single value in a set using add()method
print(a)
a=set()#creating a constructor
print(dir(a))
e={1,2,3,4,"hi"}
print(e)
e.update([7,8,9,"hello"])#using update method to update the value of set
print(e)
e.remove(2)#remove method is used to remove the specific value from a set
print(e)
e.pop()
print(e)
e.pop()
print(e)
e.pop()
print(e)
e.pop()
print(e)
e.pop()
print(e)




