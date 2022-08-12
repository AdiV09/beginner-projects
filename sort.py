li = []
type_in = input("Enter string (str) or number (float): ")

print()

if type_in == "str":
    in_ = input("Enter string: ")

else:
    in_ = float(input("Enter number: "))

while in_ != "quit" and in_ != 909:
    li.append(in_)
    if type_in == "str":
        in_ = input("Enter string: ")

    else:
        in_ = float(input("Enter number: "))

li.sort()

print(f"Sorted list: {li}")
