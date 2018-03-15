"""
import random

s  = random.randint(97, 122)
r = chr(s)
r = 'a'
print(int(r))
"""
import pprint
with open ('1.txt') as file1:
    words=file1.read()
word_ori={}
word_ori=words.split()
count={}
for word in word_ori:
    if not word[-1].isalpha:
        word = word[0:-1]
    word = word.lower()
    count.setdefault(word, 0)
    count[word] += 1
pprint.pprint(count)