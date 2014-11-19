import pytest

from hash_table import *

file = open('/usr/share/dict/words', 'r')
read = file.readlines()
file.close()
len(read)
length = len(read)
length = length * 1.6
length
int(length)
length = int(length) 
table = HashMap(length)
keylist = []
for word in read:
    keylist.append(table.hash(word))
for index, word in enumerate(read):
    table.set(keylist[index], word)
for index, word in enumerate(read):
    assert word == table.get(keylist[index])
newlist = []
for key in keylist:
    newlist.append(table.get(keylist[key]))
zip(newlist, read)