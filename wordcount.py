# put your code here.
def count_words(textfile):
    
    textfile = open(textfile)

    word_count_dict = {}

    for line in textfile:
        line = line.rstrip()
        word_list = line.split(" ")

        for word in word_list:
            word_count_dict[word] = word_count_dict.get(word, 0) + 1

    formatted_count = ""

    for word, count in word_count_dict.items():
        formatted_count = formatted_count + (f'{word} {count}') + "\n"

    return formatted_count

#print(count_words("test.txt"))
print(count_words("twain.txt"))