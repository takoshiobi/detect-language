def split(file):
    with open(file) as f:
        for line in f:
            for word in line.split():
                print (word)

### open file as : /local/iuliia.shcherbakova/Bureau/lg exemples/***filename***

import re
from collections import Counter

def most_frequent(file):
    with open(file) as f:
        passage = f.read()
        words = re.findall(r'\w+', passage)
        cap_words = [word.upper() for word in words]
        return Counter(cap_words)   
