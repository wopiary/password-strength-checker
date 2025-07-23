# length, special character, uppercase lowercase, digits, (root, admin, god), entropy estimate, 
import re

user_password = (input('Input password to test: '))

def length():
    length = len(user_password)
    if length < 8:
        print('short')
    elif length > 8:
        print('long')
length()

def specialchar():
    specials = "!@#$%^&*()_+{}[]|\\:;\"'<>,.?/~`"
    for char in specials:
        if char in user_password:
            print('special present')
            break

specialchar()

def digits():
    for char in user_password:
        if char.isdigit():
            print('numbers present')
            break
digits()

def usual():
    key_phrases = ['admin', 'god', 'root', '123456', 'password', 'qwerty']
    for keys in key_phrases:
        if keys in user_password:
            print('common present')

usual()

def charcase():
    for letter in user_password:
        if letter.islower():
            print('lower')
        elif letter.isupper():
            print('upper')
charcase()