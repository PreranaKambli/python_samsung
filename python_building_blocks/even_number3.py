#check if the use given number is Even or Odd

print("Enter a number to check if it is Even or not")
input_number = int(input())
#we have assumed 45 as the input number for the program

if input_number % 2 == 0:
    print(input_number,"is an Even number")
else:
    print(input_number, " is not an Even number")
    print(f' (input_number) is an Odd number')