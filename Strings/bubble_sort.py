import sys

def buuble_sort(numbers):
    for i in range (len(numbers)):
        sorted = True 
        for j in range(len(numbers)-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                sorted = False
        if sorted:
            return 
    

size = int(sys.argv[1])  #program starts here
numbers = []

print(f'Enter {size} numbers of the array')
for i in range(size):
    numbers.append(int(input()))

numbers.sort()
search_key = int(input('Enter the element to be searched: '))

index = bubble_sort(numbers, search_key)
print('The inpur array is: \n', numbers)
if index == -1:
    print(f'The number {search_key} was not found')
else:
    print(f'The number {search_key} was found at index {index}')
