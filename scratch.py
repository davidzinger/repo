def hang_man(word):
    list1 = []
    count_word = 0
    count_list =0

    for x in word:
        list1.append("_")
        count_word = count_word +1

    while count_list != count_word -1 :
        letter = input("write letter ")
        for z in range(count_word):
            if letter == word[z]  :
                list1.pop(z)
                list1.insert(z,letter)
                count_list = count_list + 1
            if word[z]=='_':
                count_list = count_list + 1
        print(list1)



hang_man("ss gs")
