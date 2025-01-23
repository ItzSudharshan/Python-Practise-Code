# alnum() -> Checks if all characters are alphabets or numbers (no special characters or spaces allowed)
s1 = 'kodnest1234*'
s2 = 'kodnest1234'
s3 = 'kodnest'
print("Alphanumeric Check:")
print(s1.isalnum())  # False, because of '*'
print(s2.isalnum())  # True, all characters are alphabets or digits
print(s3.isalnum())  # True, all characters are alphabets
print()

# isalpha() -> Checks if all characters are alphabets (no digits, special characters, or spaces allowed)
s1 = 'kodnest1234'
s2 = 'kodnest'
s3 = 'kod nest'
print("Alphabetical Check:")
print(s1.isalpha())  # False, because of digits
print(s2.isalpha())  # True, all characters are alphabets
print(s3.isalpha())  # False, because of space
print()

# isdigit() -> Checks if all characters are digits (no alphabets, special characters, or spaces allowed)
s1 = '12345'
s2 = '12345abc'
s3 = '123 45'
print("Digit Check:")
print(s1.isdigit())  # True, all characters are digits
print(s2.isdigit())  # False, because of alphabets
print(s3.isdigit())  # False, because of space
print()

# islower() -> Checks if all characters are lowercase (ignores non-alphabet characters)
s1 = 'kodnest'
s2 = 'Kodnest'
s3 = 'kodnest123'
print("Lowercase Check:")
print(s1.islower())  # True, all alphabets are lowercase
print(s2.islower())  # False, because of the uppercase 'K'
print(s3.islower())  # True, ignores digits
print()

# isupper() -> Checks if all characters are uppercase (ignores non-alphabet characters)
s1 = 'KODNEST'
s2 = 'Kodnest'
s3 = 'KODNEST123'
print("Uppercase Check:")
print(s1.isupper())  # True, all alphabets are uppercase
print(s2.isupper())  # False, because of the lowercase 'o'
print(s3.isupper())  # True, ignores digits
print()
