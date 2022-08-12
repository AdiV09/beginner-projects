in_string = input("Input: ")
rev_string = "".join(reversed(in_string))

if in_string == rev_string:
    print(f"'{in_string}' is a palindrome.")

else:
    print(f"'{in_string}' is not a palindrome.")
