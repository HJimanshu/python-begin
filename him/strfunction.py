#using capitalize method of the string
str="my name  is HIMANSHU"
x=str.capitalize()#The capitalize() method returns a string where the first character is upper case, and rest is lower case.
print(x)
print(str.lower())#lower method case
print(str.upper())#upper case
#using center method of the string
y=str.center(30)#the center method will center align the string ,using a specified character(space is default) as the fill character.
print(y)
y=str.center(40,"_")
print(y)
#using count method
z=str.count("a")#this method return the count of the character
print(z)
z1=str.count("m")
print(z1)
z2=str.count("a",10,20)#search from the position 10(start to 20(end)
print(z2)
#using find method
a=str.find("a")#find method finds the first occurence of specified value
print(a)
print(str.find("a",7,10))#find method return -1 if the value is not found
#using index method
a1=str.index("a")
print(a1)
# print(str.index("a",7,10))#index method work like a find method and in this just small difference when the value is not return it will raise an exception
b=str.replace("A","a")#replace method replace the specified value with the specified value.
print(b)
b1=str.replace("A","a",0)#using count of character for a specified value
print(b1)
#using split method
c=str.split("#")#split the string at the specified separator, and return a list
print(c)
print(str.title())
#using strip method
d=str.strip()#this method is used to remove any leading(spaces at the beginning) and trailing (spaces at the end) character(spaces is the default leading character to remove)
print(d)
#using format method
e="my name is {fname},my age is {age}"#The placeholder is defined using curly brackets: {}
print(e.format(fname="Himanshu",age=23))#The format() method formats the specified value(s) and insert them inside the string's placeholder.
