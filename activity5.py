"""
words_file = open('CROSSWD.txt','r')

print(type(words_file))
words = []
for line in words_file:
    #words.append(line)
    print(line.strip())
"""
# print([x for x in dir(words_file) if '_' != x[0]])

# data = [1, 3, 2, 8, 5, 6, 10]

# print([2*x for x in data if x % 2 == 0])

# print(words_file.readline())
# print(words_file.readline())

# for line in words_file:
#    print(line)


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