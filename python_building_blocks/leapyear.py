#check if user given year is a leap year or no

print("Enter a year to check if it is a leap year or not: ")
input_year = int(input())

if input_year % 4 == 0:
    print(input_year,"It is a leap year")
else:
    print(input_year,"It is not a leap year")