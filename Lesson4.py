'''
Zachary Briggs
10/30/24
Nested Loops
'''

for i in range(4):
    for j in range(3):
        print("Fromg")
# prints fromg 12 times

for row in range(5):
    for column in range(5):
        print("*")
    print()

print()
print()

for i in range(5):
    for j in range(i+1):
        print("*", end="")
    print()