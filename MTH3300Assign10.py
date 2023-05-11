"""Problem 1"""
def reversetxt(txtfile):
    file = open(txtfile, 'r')
    line_list = []
    for line in file:
        line_list.append(line)
    
    output = open("output.txt", 'w')
    for i in range(len(line_list) - 1, -1, -1):
        output.write(line_list[i])
        
    file.close()
    output.close()
    
#reversetxt("input.txt")

"""Problem 2"""
def excludechar(txtfile):
    file = open(txtfile)
    text = file.read()
    chars = {'a':0, 'b':0, 'c':0, 'd':0,'e':0, 'f':0, 'g':0, 'h':0,\
             'i':0, 'j':0, 'k':0, 'l':0,'m':0, 'n':0, 'o':0, 'p':0,\
            'q':0, 'r':0, 's':0, 't':0,'u':0, 'v':0, 'w':0, 'x':0,\
            'y':0, 'z':0 }
    for char in text:
        if char in chars:
            chars[char] += 1
    
    output = open("output.txt", 'w')
    for key in chars:
        if chars[key] == 0:
            output.write(key)
            output.write('\n')
            
    file.close()
    output.close()
            
#excludechar("input.txt")

"""Problem 3"""
def getWords(text):
    word = ""
    words = []
    start_of_word = 0
    for i in range(len(text)):
        if text[i] == '\n' or text[i] == ' ':
            words.append(text[start_of_word : i])
            start_of_word = i + 1
            word = ""
        else:
            word += text[i]
    return words

import dbm
from pickle import *
def storeWords(text):
    db = dbm.open("words.db", 'c')
    words = getWords(text)
    for word in words:
        for char in word:
            if char in db:
                char_list = loads(db[char])
                if word not in char_list:
                    char_list.append(word)
                    db[char] = dumps(char_list)
            else:
                char_list = []
                char_list.append(word)
                db[char] = dumps(char_list)
            
#storeWords("the quick brown fox jumped over the lazy dog ")

"""
def printDB(dbname):
    db = dbm.open(dbname, 'r')
    for key in db:
        print(key.decode(), ':', loads(db[key]))
        
printDB("words.db")
"""