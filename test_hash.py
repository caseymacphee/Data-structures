import pytest

from hash_table import *

def test_hash_table():
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
        keylist.append(word.rstrip())
    for word in keylist:
        table.set(word, word)
    for word in keylist:
        assert word == table.get(word)
    newlist = []