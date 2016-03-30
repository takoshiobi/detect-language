### short list only for demonstration

global_list = [['de', 'le', 'la'],['di', 'e', 'la'],
               ['und', 'die', 'er'],['der', 'den', 'in']]

#global_list[0] = "french"
#global_list[1] = "italian"
#global_list[2] = "german"


### only for demonstration

def split(file):
    with open(file) as f:
        words = [word for line in f for word in line.split()]
        print(words) # returns a list of words

### this function was used for make a global_list 
        
def common_three(file):
    with open(file) as f:
        word_list = [word for line in f for word in line.split()]
    word_counter = {}
    for word in word_list:
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1

    popular_words = sorted(word_counter, key = word_counter.get, reverse = True)
    top_three = popular_words[:3]
    return top_three # returns 3 most common words of text

### step 1

def common_input(chaine):
    assert type(chaine) == str
    listed = chaine.split()
    word_counter = {}
    for word in listed:
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1

    popular_words = sorted(word_counter, key = word_counter.get, reverse = True)
    top_three = popular_words[:3]
    return top_three # returns 3 most common words of str

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
    top_three = popular_words[:3]

    if top_three[0] == global_list[0][0] or top_three[0] == global_list[0][1] or top_three[0] == global_list[0][2]:
        print("french")
    elif top_three[0] == global_list[1][0] or top_three[0] == global_list[1][1] or top_three[0] == global_list[1][2]:
        print("italian")
    else: #there is no such function in final program
        print("german")
