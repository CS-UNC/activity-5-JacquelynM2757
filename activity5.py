# FUNCTION 1:

def more_than_20(file):
    words = []
    data = open(file, 'r')
    #for word in data:
    #    if len(word.strip()) > 20:
    #        words.append(word.strip())
    words = [x.strip() for x in data if len(x.strip()) > 20]
    return words

print(more_than_20("CROSSWD.txt"))

# FUNCTION 2:

def has_no_e(word):
    if 'e' in word:
        return False
    else:
        return True
print (has_no_e("abracadabra"))

# FUNCTION 3:

def uses_only(word, letters):
    for x in word:
        if x not in letters:
            return False 
    return True
print(uses_only("banana", "bn")) 

# FUNCTION 4:

def all_uses_only(file, letters):
    result = []
    with open(file, 'r') as f:
        for line in f:
            word = line.strip()
            if uses_only(word, letters):
                result.append(word)
    return result


print(all_uses_only("CROSSWD.txt", 'abn'))