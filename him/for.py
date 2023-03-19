#why For loop is used.
#For loop is used when the number of iterations is already known,the for loop is used.
#syntax
#for value in range/sequence:
       # loop body
#code to find the sum of squares of each element of the list using for loop.
#creating the list of numbers.
numbers= [3,4,5,6,7,8,9]
#initializing a variable that will store the sum.
sum_=0
#using for loop to iterate over the list.
# for num in numbers :
#     sum_=sum_ + num**2
# print("The sum of squares is:",sum_)
#in this using range()method
#range() function returns a sequence of numbers,starting from 0 by default, and increments by 1(by default),and stop before a specified number.
for num in range(len(numbers)):
    sum_=sum_ + numbers[num]**2
print("The sum of squares is:",sum_)
