#Task : A cybersecurity training institute issues a Cybersecurity Awareness Certificate only to candidates who meet the required criteria, Write a code.
# Type your code below

# 1. Get input from the user and convert to numbers
Score = int(input("Enter your score: "))
Age = int(input("Enter your age: "))

# 2. Check eligibility (your fixed logic)
if Score >= 60 and Age >= 18:
    print("Eligible for Certificate")
else:
    print("Not Eligible for Certificate")
