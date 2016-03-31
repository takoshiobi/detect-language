### frequent words by common_words:

## german

# >>> common_words("de1",3)
#['der', 'mit', 'in']
#>>> common_words("de2",3)
#['der', 'den', 'er']
#>>> common_words("de3",3)
#['und', 'die', 'er']
#>>> common_words("de4",3)
#['die', 'der', 'in']
#>>> common_words("de5",3)
#['die', 'der', 'und']

# 7 most frequent words (pour allemand) : der, mit, in, den, er, und, die

## etc for common_words

# pour espagnol : de, el, la, que, en
# français : de, le, des, la, à
# italian : di, e, la, che, il, per
# swedish : att, i, och, är, på, en, som
# UK English : the, to, and, he, of, in

global_list = [['der', 'mit', 'in', 'den', 'er', 'und', 'die'],
               ['de', 'el', 'la', 'que', 'en'],
               ['de', 'le', 'des', 'la', 'à'],
               ['di', 'e', 'la', 'che', 'il', 'per'],
               ['att', 'i', 'och', 'är', 'på', 'en', 'som'],
               ['the', 'to', 'and', 'he', 'of', 'in']]
               

#global_list[0] = "german"
#global_list[1] = "espagnol"
#global_list[2] = "français" ... etc.


### only for demonstration

def split(file):
    with open(file) as f:
        words = [word for line in f for word in line.split()]
        print(words) # returns a list of words

### this function was used for global_list 
        
def common_words(file,n):
    with open(file) as f:
        word_list = [word for line in f for word in line.split()]
    word_counter = {}
    for word in word_list:
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1

    popular_words = sorted(word_counter, key = word_counter.get, reverse = True)
    top_three = popular_words[:n]
    return top_three # returns n most common words of text

### step 1

def common_input(chaine,n):
    assert type(chaine) == str
    listed = chaine.split()
    word_counter = {}
    for word in listed:
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1

    popular_words = sorted(word_counter, key = word_counter.get, reverse = True)
    top_three = popular_words[:n]
    return top_three # returns n most common words of str

### final function

def final_detection(chaine):
    assert type(chaine) == str
    listed = chaine.split()
    word_counter = {}
    for word in listed:
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1

    popular_words = sorted(word_counter, key = word_counter.get, reverse = True)
    top_three = popular_words[:1]

    if top_three[0] == global_list[0][0] or top_three[0] == global_list[0][1] or top_three[0] == global_list[0][2] or top_three[0] == global_list[0][3] or top_three[0] == global_list[0][4] or top_three[0] == global_list[0][5] or top_three[0] == global_list[0][6]:
        print("German")
    elif top_three[0] == global_list[1][0] or top_three[0] == global_list[1][1] or top_three[0] == global_list[1][3] or top_three[0] == global_list[1][4]:
        print("Espagnol")
    elif top_three[0] == global_list[2][0] or top_three[0] == global_list[2][1] or top_three[0] == global_list[2][2] or top_three[0] == global_list[2][3] or top_three[0] == global_list[2][4]:
        print("French")
    elif top_three[0] == global_list[3][0] or top_three[0] == global_list[3][1] or top_three[0] == global_list[3][2] or top_three[0] == global_list[3][3] or top_three[0] == global_list[3][4] or top_three[0] == global_list[3][5]:
        print("Italian")
    elif top_three[0] == global_list[4][0] or top_three[0] == global_list[4][1] or top_three[0] == global_list[4][2] or top_three[0] == global_list[4][3] or top_three[0] == global_list[4][4] or top_three[0] == global_list[4][5] or top_three[0] == global_list[4][6]:
        print("Swedish")
    elif top_three[0] == global_list[5][0] or top_three[0] == global_list[5][1] or top_three[0] == global_list[5][2] or top_three[0] == global_list[5][3] or top_three[0] == global_list[5][4] or top_three[0] == global_list[5][5]:
        print("English")
    else:
        return False
