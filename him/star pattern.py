# n=5
# i=1
# j=0
# while i<=n:
#
#     while j<=i-1:
#         k=0
#         while k <= j:
#            print("-",end="")
# #            k+=1
# #         print("* ",end="")
# #         j+=1
# #     print("\r")
# #     j=0
# #     i+=1
n=5
i1=1
j1=0
while i1<=n:
    while j1<=i1-1:
        print(" *",end=" ")
        j1+=1
    print("\r")
    j1=0
    i1+=1
# # #
# # # def pattern (a):
# # #     i=a
# # #     while i>=a:
# # #         print(" "* (a-i) +"*" * i)
# # # n = int(input("Enter the number of the row:"))
# # # pattern('a')
# n= int(input("enter the number of row:"))
# row=0
# while row<n:
#     space=n-row-1
#     while space>0:
#         print(end=" ")
#         space-=1
#     star=row+1
#     while star>0:
#         print("*",end=" ")
#         star-=1
#     row=row+1
#     print()

#factorial of given number
# num=7
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print("the factorial of",num,"is",fact)
#
# #fabonacci series of specific number
# # n=int(input("enter the number:"))
# def fibonacci(n):
#     if n<0:
#         print("Incorrect input")
#     elif n == 0:
#         return 0
#     elif n == 1 & n == 2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(9))
# list=[1,2,3,4]
# print(list)
# print(list.remove(2))#it remove the matching element.don't return the remove element
# print(list)
# print(list.pop(2))#it removes the element by indexe,also return the remove element
# print(list)
# li=[1,2,3,4]
# print(del li[1])#usinf del method doesn't return any value.
# # print(list)
