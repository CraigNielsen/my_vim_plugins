
def wrap_word_in_quotes(word):
    return "'{0}': ".format(word)
def convert_to_dict(string):
    index = 0
    final = ''
    sp = string.split()
    for i in sp:
        if (index%2 == 0):
            final+=(wrap_word_in_quotes(i))
        else:
            final+=(i)
            final+=(', ')
        index +=1
    return final[:-2]
