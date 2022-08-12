in_string = input("Enter string: ")
used = []
duplicates = []

for char in in_string:
    char = char.lower()
    if char not in used:
        used += char

    else:
        if char not in duplicates:
            duplicates += char

print(duplicates)
