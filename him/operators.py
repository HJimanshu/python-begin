#different types of python operators
'''1.Arithmetic operators
2.Assignment Operators
3.Comparison Operators
4.Logical Operators
5.Bitwise Operators
6.Special Operators'''
a=10
b=4
c=5
#1.Arithmetic Operators
add=a+b
sub=a-b
mul=a*b
div=a/b
floordiv=a//b
mod=a%b
pow=a**2
print(add)
print(sub)
print(mul)
print(div)
print(floordiv)
print(mod)
print(pow)
#2.Assignment Operators
print(c)#assignment operator:-->> (=)
c+=1
print(c)#Addition Assignment:-->> (+=)
c-=1#Subtraction Assignment:-->> (-=)
print(c)
c*=2#multiplication Assignment:-->> (*=)
print(c)
c/=2#Division Assignment:-->> (/=)
print(c)
c%=2#Remainder Assignment:-->> (%=)
print(c)
c**=2#Exponent Assignment:-->> (**=)
print(c)
# 3.Comparison Operators
print(a==b)#Is Equal to
print(a!=b)#Not Equal to
print(a>b)#Greater than
print(a<b)#Less Than
print(a>=b)#Greater Than or Equal To
print(a<=b)#Less Than or Equal to
#4.Logical Operators
print("\n",(a>2)and(b>=4))#Logical AND:->True only if both the operands are true
print((a>4)or(b>=6))#Logical or:->True if at least one of the operands is true
print(not b)#Logical Not:--> true if operand is false and vice-versa.
# 5.Bitwise Operators
print(a&b)#Bitwise AND
print(a|b)#Bitwise OR
print(~b)#Bitwise NOT
print(a^b)#Bitwise XOR
print(a>>b)#Bitwise right shift
print(a<<b)#Bitwise Left shift
#6.Special operators
x1=3
y1=3
x2='hello'
y2='hello'
x3=[1,2,3]
y3=[1,2,3]
print(x1 is not y1)# true if the operands are not identical(do not refer to the same object
print(x1 is y1)#true if operands are identical (refer to the same object)
#write a program using membership operators in python
print(2 not in y3)#return true if a sequence with the specified value is not present in the list
print(1 in x3)#return true if a sequence with the value 1 is in the list
print(0 not in y3)#return true if a sequence with the value is not in the list