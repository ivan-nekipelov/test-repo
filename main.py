number = int(input("Please enter the number:"))
fourth_digit = number % 10
number = number // 10
third_number = number % 10
number = number // 10
second_number = number % 10
number = number // 10
first_number = number % 10

print(first_number)
print(second_number)
print(third_number)
print(fourth_digit)
