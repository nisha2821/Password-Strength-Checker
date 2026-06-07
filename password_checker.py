 
password = input("Enter your password: ")
has_upper=False
has_lower=False
has_digit=False
has_special=False
for char in password:
    if char.isupper():
        has_upper=True
    if char.islower():
        has_lower=True
    if char.isdigit():
        has_digit=True
    if char in "!@#$%^&*":
        has_special=True
if len(password)>=8 and has_upper and has_lower and has_digit and has_special:
    print("strong password.")
else:
    print("weak password.")


