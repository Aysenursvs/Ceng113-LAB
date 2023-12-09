def longest_common_prefix():
    str_list = []
    answer = "y"

    while answer == "y":
        string_user = input("Enter a word: ")
        str_list.append(string_user)
        answer = input("Do you want to enter a word? (y/n): ")

    str_list.sort()

    first_element = str_list[0]
    last_element = str_list[len(str_list) - 1]

    common_prefix = []

    for i in range(len(first_element)):
        if i < len(last_element) and first_element[i] == last_element[i]:
            common_prefix.append(first_element[i])

    prefix = ""
    for i in common_prefix:
        prefix += i

    return "The longest commen prefix {}.".format(prefix)

print(longest_common_prefix())



