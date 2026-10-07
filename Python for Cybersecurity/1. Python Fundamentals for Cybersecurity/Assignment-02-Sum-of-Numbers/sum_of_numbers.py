# Write a program calculate the sum of event counts from 1 to n.
# Type your code below

# Get the value of n from the user
n = int(input("Enter a number: "))

total = 0
for i in range(1, n + 1):
    total += i

print(total)
