'''
Name: Zachary Briggs
Date: 10/22/24
Description: Unit 4 Lesson 1 - while loops

'''

# while loops  run while a condition is true
# we usually don't know how many times, this scenario
# is when they are most often used

'''
some_boolean

while some_boolean is true:
    code to execute
    update variable (if forgotten -> infinite loop)
'''

start_number = 10
while start_number >= 0:
    print(start_number)
    start_number = start_number-1
print('Blastoff!')

while True:
    user_age = int(input("Enter age or -1 to quit: "))
    if user_age == -1:
        break #exits the loop
    else:
        continue #return to top of loop