
import sys
def binary_searh(numbers,search_key):
     
size=int(sys.argv[1])
number = []
search_key = 0
print(f'enter {size} number of the array')
for i in range (size):
     number.append(int(input()))
search_key=int(input("enter the element to be searched"))     
index = binary_search(number,search_key)
if index == -1:
     print(f"the number {search_key} was not found")
else:
     print(f"the number{search_key}was found at the index{index}")



