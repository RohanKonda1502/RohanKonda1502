"""import math
# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Print all prime numbers up to 50
for number in range(51):
    if is_prime(number):
        print(number)
# Calculate the sum of all even numbers from 1 to 20
total_sum = 0
for number in range(1, 21):
    if number % 2 == 0:
        total_sum += number

print("The sum of all even numbers from 1 to 20 is:", total_sum)
# Calculate the sum of all odd numbers from 1 to 20
total_sum = 0
for number in range(1, 21):
    if number % 3 == 0:
        total_sum += number

print("The sum of all odd numbers from 1 to 20 is:", total_sum)
# Function to reverse a string
def reverse_string(s):
    return s[::-1]

# Get user input
user_input = input("Enter a string: ")

# Reverse the string and print the result
reversed_string = reverse_string(user_input)
print("Reversed string:", reversed_string)
print("Hi, John!")
print(1 + 2)
Inputname = input("What is your name? ")
print("Hello, " + Inputname + "!")
print("Namaste", end=", ")
print("India")
#greatest of two integers
a=int(input('enter number 1='))
b=int(input('enter number 2='))
if a>b:
    print("a is greater")
elif a==b:print("both are equal")
else:print("b is greater")
#to check a given number is even or odd
A=int(input('enter a number='))
if A%2==0:
    print("the given number is even")
else:
    print("the given number is odd")
#grading for marks
A=int(input('please enter your mark'))
if A>=90:
    print('grade A+')
name = 'Hari'
age = 18

print(name, ', you are ', age, ' now but ', end="")
print('You will be ', age + 1, ' next Year')
#volume of a cylinder
R=int(input('enter radius:'))
H=int(input('enter height:'))
vol=math.pi*R*R*H
print('volume of a cylinder=',vol)

#while loop
z = 0

while z < 3:
    if z == 0:
        print("z is",z)
        z += 1
    elif z == 1:
        print("z is",z)
        z += 1
    else:
        print("z is",z)
z += 1
#nested loop
for a in range(3):
    for b in range(10):
        print("@",end='')
    print()"""
'''#my PT-3 practice
A=int(input('enter a Number'))
if A%2==0:
    print('it is an EVEN Number')
else:
    print('it is an ODD number')
#largest of three numbers
A=float(input('Enter First Number:'))
B=float(input('Enter Second Number:'))
C=float(input('Enter Third Number:'))
if A>B:
    print(int(A),'is greatest among 3 numbers')
elif B>C:
    print(int(B),'is greatest among 3 numbers')
elif C>A:
    print(int(C),'is greatest among 3 numbers')'''
