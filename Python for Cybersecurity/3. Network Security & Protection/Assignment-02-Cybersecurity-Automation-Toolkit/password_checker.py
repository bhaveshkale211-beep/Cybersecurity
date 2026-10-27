import string

# Check the strength of a password entered by the user

password = input("\nEnter your password to check the strength of your password ! \n ")

has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_number = any(char.isdigit() for char in password)
has_special = any(char in string.punctuation for char in password)

score = 0

if len(password) >= 8:
    score += 1

if has_upper:
    score += 1

if has_lower:
    score += 1

if has_number:
    score += 1

if has_special:
    score += 1

print("\nPassword Analysis")
print("------------------")
print("Length:", len(password))
print("Uppercase:", has_upper)
print("Lowercase:", has_lower)
print("Number:", has_number)
print("Special Character:", has_special)

if score <= 2:
    print("\n Password Strength: Weak")
elif score <= 4:
    print("\n Password Strength: Moderate")
else:
    print("\n Password Strength: Strong\n")
print("\n")


