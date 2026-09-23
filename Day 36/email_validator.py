# Validating the email using regular expressions.
import re
while True:
    pattern =r"[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net|org)"
    user_input = input("Enter the valid email: ")
    if re.match(pattern,user_input):
        print(f"'{user_input}'is an valid email")
        break
        
    else:
        print(f"'{user_input}' was not found,Invalid email")
        continue