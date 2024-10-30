'''
Name: Zachary Briggs
Date: 10/24/24
Description: For loops
'''
from numba.cpython.randomimpl import np_gauss_impl1

# For loop style 1 - for in in range(stop)

for i in range(5):
    print(i)

# prints 0, 1, 2, 3, 4 all on their own lines.
# the number in range means how many numbers are printed
# starting at 0 and ending at stop-1
# common use: doing a known number of things

# numbers on the same line:
for i in range(5):
    print(i,end=" ") #can also add a comma in the middle, also you can do
# for i etc twice just make sure to add a line inbetween and say print() so theres a break
# and so it's not pushed together

# Method 2: for i in range(start, stop)
# doesn't have to be i
for num in range(2,6):
    print("*"*num)
print()
for num in range (2,6):
    print(num,end="  ")
##################
print()
print(f"Number x|x^2")
print("_____")
for num_to_square in range(1,6):
    print(f"{num_to_square} | {num_to_square**2}")
print(f"------")

# prints start, start+1, ...., stop-1
# loop runs stop-start number of times.

print()

# Method 3: for i in range (start,stop,step)
# this prints start, start+1, ...., stop-1 but counts by step
# loop runs ceiling((stop-start)/step) (round up) times
# ceiling means round up to the neatest int
for number in range(10,40,4): # want: 10-40 counting by 4's
    print(number, end=" ")

# want: start at 12, count by 7s up to but not past 93
print()
for number in range(12,93,7):
    print(number,end=" ")

##################################################

#print the sum of the numbers 0 through n
print()
user_num = int(input("Give me a number"))
sum = 0 # initialize our sum to 0
for num in range(1, user_num+1):
    sum = sum+num
print(f"The sum is {sum}")

##################################################
# 1) ask the user to enter 5 numbers
# 2) find the average of those numbers (hint: use a loop)
# 3) print "The average of your numbers is ----"
print()

num1= int(input("Enter a number:"))
num2= int(input("Enter a number:"))
num3= int(input("Enter a number:"))
num4= int(input("Enter a number:"))
num5= int(input("Enter a number:"))

average = ((num1+num2+num3+num4+num5)/5)
print("The average of your numbers is",average)
# can also do it like this
average1= 0

for num in range(num1, num5+1):
    average1=((num1+num2+num3+num4+num5)/5)
print("The average of your numbers is", average1)

# Another solution:
sum1=0
num_values=5 #allows you to modify and make the range what the user wants (see line 93)
for i in range(5):
    user_num = int(input("Enter a number:"))
    sum1 = sum1 +user_num
average2 = sum1/num_values
print("The average of your numbers is", average2)

#Write program that makes user guess a number between 1 and 100 save number in variable called magic_number
#If user guesses a number higher than secret number     if user guesses number lower than the secret number

import random

magic_number = random.randint(1,1000)
try_count = 0
while True:
    user_guess = int(input("Guess the magic number!"))
    if user_guess > magic_number:
        print("Too high")
        try_count += 1
    elif user_guess < magic_number:
        print("Too low")
        try_count += 1
    elif user_guess == magic_number:
        print("You got it!")
        break
    if try_count == 7:
        print(f"Try again! The magic number was {magic_number}")
        break