a=(1,2,3,4,5,2,2)
print(a)#print the sets literals
print(type(a))#using type casting we can understand the types of literals
print(a[2])
#a[1]=2:->>>>tuple does not support item assignment therefore tuple is immutable
print(dir(a))
b=(1,2,"hii","hello",2.3)
print(b)
print(b[2:3])#using slicing in tuple data structure
c=a+b
print(c)#concatination is also possible in tuple
print(len(a))
print(a.count(2))#the count method tells us about the value,how many timesa that value is repeated or given
print(b.index(2.3))#using index method ,it will give the index position
g=(1,'hii',{1},{1:"hiii"})
print(type(g[2]))
# print(g)