def find_pattern(sentence, substring):
    length_of_sentence = len(sentence)
    length_of_substring = len(substring)
    test_string = ''

    for i in range(length_of_sentence):
        for j in range(i, length_of_substring+i):
            test_string += sentence[j]
        # print(test_string)
        if test_string == substring:
            return True
        test_string = ''

    return False


print(find_pattern('forever', 'ever'))
