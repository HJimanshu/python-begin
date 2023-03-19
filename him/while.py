# why to use while loop
#While loop is used when the number of iterations is already Unknown.
count=0
while count<3:
    count=count+1
    print("Hello")
    # count=0#1.with count=0
    #2.without count=0
    while count < 3:#Example of nested while loop
        count = count + 1
        print("Hello")
else: #using else statement with while loop
    print("Nested while loop are terminated ")

count=1
while count < 3:#example of simple while loop
        count = count + 1
        print("\n\nHello")
#using loop control statements:-> continue,break and pass
count1=1
while count1 < 3:
        count1 = count1 + 1
        print("\nHello guys")
        while count1 < 3:
            # break
            #break statement:->>it terminate the current loop
            # continue
            # continue statement:->> skip the flow of the program for next iteration
            def mypass():
                pass#pass statement is used in funtion definition

            # the pass statement is used as a placeholder for future code.
            ''' when the pass statements is executed ,nothing happens, but you avoid getting an error when empty code is not allowed. 
            Empty code is not allowed in loops,function definitions,or in ifstatements'''
            count1 = count1 + 1
            print("Hello")
else: print("while loop are complete")
i = 1
while True:
     if i%3 == 0:
         break
     print(i)
     i += 1

