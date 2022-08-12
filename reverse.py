in_type = input("Will you input a string (str) or an integer (int)?: ")
if in_type == "str":
    in_ = input("Enter string: ")
    rev_in = "".join(reversed(in_))

else:
    in_ = int(input("Enter number: "))
    rev_in = "".join(reversed(str(in_)))
    rev_in = int(rev_in)

print(rev_in)
