list1 =[]
list2 = list()
list1.append(10)
list1.append(20)
list1.insert(1,30)
print(list1)
print("popped element is",list1.pop())
list1.extend([10,19])
print(list1)

list2 = list(list1)
del list2[0]
print(f'list1 = {list1} \n list2 = {list2}')
list1.clear()
print(list1)
del list1
#print(list1)#NameError
print("sum of list2 elements =",sum(list2))
print("length of list2 is ", len(list2))
print("type of list2 is ",type(list2))
list2 = [12,3,9,5,4]
print(list2)
print("sorted list2 = ",sorted(list2))#sorted is a function. it returns
list2.sort()# sort is a method it does not return 
print(list2)
print(f'index of 5 in list2 ={list2.index(5)}')