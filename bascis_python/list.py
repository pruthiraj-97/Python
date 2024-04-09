# list1=[1,2,3,4]
# list2=list1 # reference copy list1 and list2 have same 
# print(list1) # reference of list1 and list2 are same
# list1[0]=60
# print(list2)

# x="py"
# y=x
# x="js"    
# print(y)

list1=[1,2,3,4,5]
list2=list1[:] # shallow copy list1 and list2 are diff
print(list2)
list1[2]=88
print(list2)
# same for list and tuple and dict