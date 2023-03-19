a={1:"hii",2:"i",3:"am",4:"Hiamnshu"}
print(a)#print dictionary
print(a[3])#indexing is done  by keys
print(a[2])#example of indexing is done by key
b={'A':"who",'B':"are",'C':"you"}
print(b)
#another way to done indexing in dictionary
print(b.get('C'))
#dictionary are the mutable that means value can be changed
b['B']="R"#key are immutable  and dictionary values are mutable
print(b)
print(dir(a))
#some method are used in dictionary
print(a.keys())
print(b.keys())#key method is used to display the keys
print(a.values())#values method is used to display the values
print(b.values())
print(a.items())#item method display the list of the items
print(b.items())
#using pop method to remove the key and  value from the dictionary
print(a.pop(2))
print(a)
print(b.pop('A'))
print(b)
