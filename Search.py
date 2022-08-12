names = ["Add names here!"]
work_names = []

for a in names:
    work_names.append(a.lower())


def find(check_search, to_search):
    index = 0
    result = True

    for i in check_search:
        if i != to_search[index]:
            result = False

        index += 1

    return result


search = None

while search != "quit":
    search = input("Search: ")
    search = search.lower()
    search_names = []

    for n in work_names:
        if find(search, n):
            search_names.append(n)

    print(search_names)
    print()
