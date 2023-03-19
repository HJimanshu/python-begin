#write a program to find second largest number in array
list1=[34,5,2,55,33,33,99]
list2=list(set(list1))#using set method to removing the duplicate values from the list
list1.sort()#sorting the list
print("second largest number in the list",list1[-1])
# write the second example in the python to print the even and odd number
i=int(input("enter the number:"))
if i%2==0:
    print("entered value is even:")
else:
    print("entered value is odd")

