# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 14:40:57 2023

@author: kevin
"""
def mostCommon(text):
    alphabet = {}
    for char in text:
        if char.islower():
            if char not in alphabet:
                alphabet[char] = 1
            else:
                alphabet[char] += 1
    
    most = 0
    most_key = ''
    for key in alphabet:
        if alphabet[key] > most:
            most = alphabet[key]
            most_key = key
    return most_key

def findk(most_key):
    num = ord('e') - ord(most_key)
    if num < 0:
        return num + 26
    return num

def convertChar(char, key):
    num = ord(char) + key
    if num > ord('z'):
        num -= 26
    return chr(num)

def decrypt(text, key):
    clear = ''
    for char in text:
        if char.islower():
            clear += convertChar(char, key)
        else:
            clear += char
    return clear

def read(txtfile):
    f = open(txtfile)
    most_common_key = mostCommon(f.read())
    f.seek(0)
    k = findk(most_common_key)
    print(decrypt(f.read(), k))
    
#read('cipher1.txt')
#read('cipher2.txt')

def readScrabble():
    f = open('scrabble.txt')
    letters = {}
    for line in f:
        elements = line.split()
        letters[elements[0]] = int(elements[1])
    return letters

def getValue(word):
    letters = readScrabble()
    value = 0
    for char in word:
        value += letters[char]
    return value

#print(getValue('banana', letters))
            
def sort(*args):
    sorted_list = list(args)
    sorted_list.sort(key = getValue)
    
    return sorted_list

#print(sort('pineapple', 'banana', 'melon', 'papaya', 'lychee', 'coconut'))