#write a code to understand list data structure in python
a=[1,2,3,4,5]#we can declared list using square bracket
b=[1,2,4,76,34,"hii","hello"]#in which collection of values with same and different types
print(a)#print list a[]
print(b)#print list b[] using same and different types of value
print(a[4])#using indexing ,value can be fetched using indexing
print(b[1:4])#using slicing
a[1]=4#list data structure is mutable in nature.
print(a)
d=[1,2,0]
c=(a+b+d)#using + operator for concatinate two and more list
print(c)
c.append(23)#append method is used to adding the new value in the end of th list
print(c)
a.append(23)
print(a)
b.insert(2,23)#using insert method for adding the value in specific index
print(b)
c.clear()#using this method be can return empty ist[]
print(c)
print(dir(a))#dir() method used for show the all directory

print(len(a))#len()methode is used for calculating the length of the list
print(b.count("hii"))#count method is provide the counting the value of list etc...............