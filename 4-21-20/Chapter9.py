'''

import requests
url = 'http://thinkpython2.com/code/words.txt'
r = requests.get(url, allow_redirects=True)
open('words.txt', 'wb').write(r.content)
'''

fin = open('words.txt')
l = fin.readline()
l2 = l.strip()
print(l2)
l = fin.readline()
print(l)

#for line in fin:
#    word = line.strip()
#    print(word)

#determine if a specified word has an e in it
def has_no_letter(word,testletter):
    for letter in word:
        if letter == testletter:
            return False
    return True

print(has_no_letter('will','e'))
print(has_no_letter('well','l'))

#determine if word contains any forbidden letters
def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True

print(avoids('manipulate','srp'))