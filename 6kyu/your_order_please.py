def order(sentence):
    list_word = []
    new_list = []
    count = 0
    list_number = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    new_sentence = ""
    list_word = sentence.split()
    for word in list_word:
        new_list.append(word)

    for word in list_word:

        for letter in word:

            if letter in list_number:
                new_list[int(letter) - 1] = word

    for new_word in new_list:
        if count <= len(new_list) - 2:
            new_sentence += new_word + " "
            count += 1

    if len(list_word) != 0:
        new_sentence = new_sentence + new_list[len(new_list) - 1]

    return new_sentence
