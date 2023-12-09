def repeated():
    user_string = input("Enter what you want :): ")
    count = 1
    new_str = ""

    for i in range(len(user_string) - 1):
        if user_string[i] == user_string[i + 1]:
            count += 1
        else:
            new_str += user_string[i]
            new_str += str(count)
            count = 1
    new_str += user_string[len(user_string) - 1]
    new_str += str(count)
    
    return new_str

print(repeated())

#Example: input: aaabbccc  output: a3b2c3