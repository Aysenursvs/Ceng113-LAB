def anagram():
    word1 = input("Enter a word: ")
    word2 = input("Enter a word: ")
    list1 = []
    list2 = []
    for i in word1:
        list1.append(i)
    print(list1)

    for i in word2:
        list2.append(i)
    print(list2)

    anagram = True

    if len(list1) == len(list2):
        for i in list1:
            if i in list2:
                pass
            else:
                anagram = False
    else:
        anagram = False

    if anagram:
        print("{} and {} are anagram.".format(word1, word2))
    else:
        print("{} and {} are not anagram.".format(word1, word2))

anagram()