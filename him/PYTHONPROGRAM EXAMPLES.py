#First Example
# str="sky is blue"

# str1=str.split( )#split () method is used to split the string into the list
# print(str1)
# str2=str1[::-1]#slicing is used for return the slicing object ,slicing is used to return the range of the character by using the slice syntax.
# #A slice object is used to specify how to slice a sequence.
# print(str2)
# str3=" ".join(str2)#join the all items list to the string.
# #join method takes all items is an iterable and join them into one string.
# print(str3)#final output.

#print program in one line
# print( " ".join(str.split()[::-1]))

#Second Example
# list=[1,2,2,3,3,4,5,5,5,6,6]
# OUT=[1,4]
# TRY USING TYPE CASTING AND SLICING OF THE LIST ITEM
list1=[1,2,2,3,3,4,5,5,2,6,6]
list2=list(set(list1))#output will be{1,2,3,4,5,6}
print(list2[0:4:3])
#TRY ANOTHER WAY TO SOLVE THIS EXAMPLE
mylist=[1,2,2,3,3,4,5,5,5,6,6]
new_list=[]
for num in mylist:
     if mylist.count(num)==1:
         new_list.append(num)
print(new_list)

#Third Example
mystr="a,a,a,b,b,c,c,c"
# out--> a:3,b=2,c:3
# print("a:{v1}".format(v1=mystr.count('a')),"b:{v2}".format(v2=mystr.count('b')),"c:{v3}".format(v3=mystr.count('c')))
#try another way to solve this question
mylist=mystr.split(',')
print(mylist)
visited=[]
final_list=[]
for out in mylist:
    if out not in visited:
        final_list.append(f"{out}:{mylist.count(out)}")
        visited.append(out)
    print(final_list)
    print(",".join(final_list))
