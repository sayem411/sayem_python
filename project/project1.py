#Strong password
password = input("Enter password: ")

has_upper=False
has_lower=False
has_digit=False
has_special=False

for i in password:
    if i.isupper():
        has_upper=True
    elif i.islower():
        has_lower=True
    elif i.isdigit():
        has_digit=True
    else:
        has_special=True     

if has_upper and has_lower and has_digit and has_special and len(password) >= 8:
    print("Strong password ")
else:
    print("Weak password ")
    
    if not has_upper:
        print("— Add uppercase letter (A-Z)")
    if not has_lower:
        print("— Add lowercase letter (a-z)")
    if not has_digit:
        print("— Add a number (0-9)")
    if not has_special:
        print("— Add special character (!@#$...)")
    if len(password) < 8:
        print("— Minimum 8 characters required")
