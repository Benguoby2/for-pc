
"""
def func():
    for i in range(0, 101):
        if i == 0:
            print(i, end =',')
        elif (i % 3 == 0 ) and (i % 5 == 0):
            print('FizzBuzz', end =',')
        elif i % 3 == 0:
            print('Fizz', end =',')
        elif i % 5 == 0:
            print('Buzz', end =',')

        else:
            print(i, end =',')

func()
"""
"""
import random, string

def have_num(num):
    if isinstance(num, int) and num > 0 :
        _len = num
        _len_num = random.randint(0, num)
        _len_ENG = random.randint(0, num-_len_num)
        _len_eng = _len - _len_num - _len_ENG
        _len_nums = [x for x in range(0, _len_num + 1)]
        _len_engs = [x for x in range(0, _len_eng + 1)]
        _len_ENGS = [x for x in range(0, _len_ENG + 1)]
        for i in range(_len_num):
            _len_nums[i] = random.randint(0, 9)
        _len_nums.pop()
        for i in range(_len_eng):
            a = random.randint(65, 90)
            _len_engs[i] = chr(a)
            #print(chr(a))
        _len_engs.pop()
        for i in range(_len_ENG):
            a = random.randint(97, 122)
            _len_ENGS[i] = chr(a)
            #print(chr(a))
        _len_ENGS.pop()
        _len_total = _len_engs + _len_nums + _len_ENGS
        random.shuffle(_len_total)
        for i in range(num):
            if isinstance(_len_total[i], int):
                _len_total[i] = str(_len_total[i])
        _len_total = ''.join(_len_total)
        print(_len_total)
        assert len(_len_total) == num
        return _len_total
    else:
        print("请输入正整数")
have_num(250)
"""
"""
import pprint
f = open('1.txt', 'r')

word = {}
for line in f.readlines():
    if ',' or '.' or '!' or ':' or ';' or '"' or '(' or ")" or "$" or '1' \
            or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' or '0'in line:
        line = line.replace(',', '');line = line.replace('.', '');
        line = line.replace('!', '');line = line.replace(':', '');
        line = line.replace('"', '');line = line.replace(';', '');
        line = line.replace('(', '');line = line.replace(')', '');
        line = line.replace('$', '');line = line.replace('?', '');
        line = line.replace('0', '');line = line.replace('1', '');
        line = line.replace('2', '');line = line.replace('3', '');
        line = line.replace('4', '');line = line.replace('5', '');
        line = line.replace('6', '');line = line.replace('7', '');
        line = line.replace('8', '');line = line.replace('9', '');
    line = line.replace('\n', '')
    words = line.split(' ')
    for word_ready in words:
        if word.get(word_ready, 0):
            word[word_ready.lower()] = word[word_ready.lower()] + 1
        else:
            word[word_ready.lower()] = 1
word.pop('')
#pprint.pprint(word)
print(word)
"""

import random, string

src_digits = string.digits + string.ascii_lowercase + string.ascii_uppercase
password = random.sample(src_digits, 10)
random.shuffle(password)
a = ''.join(password)

print(a)






