# length, special character, uppercase lowercase, digits, (root, admin, god), entropy estimate, 
import re

# user_password = (input('Input password to test: '))

# def length():
#     length = len(user_password)
#     if length < 8:
#         print('short')
#     elif length > 8:
#         print('long')

# def specialchar():
#     specials = "!@#$%^&*()_+{}[]|\\:;\"'<>,.?/~`"
#     for char in specials:
#         if char in user_password:
#             print('special present')
#             break

# specialchar()

# def digits():
#     for char in user_password:
#         if char.isdigit():
#             print('numbers present')
#             break
# digits()

# def usual():
#     key_phrases = ['admin', 'god', 'root', '123456', 'password', 'qwerty']
#     for keys in key_phrases:
#         if keys in user_password:
#             print('common present')

# usual()

# def charcase():
    # for letter in user_password:
    #     if letter.islower():
    #         print('lower')
    #     elif letter.isupper():
    #         print('upper')
# charcase()

#CLEARTEXT RISK, ENCRYPTED GATE, QUANTUM VAULT

user_password = (input('Input password to test: '))
strength_label = ['ClearText Risk', 'Encrypted Gate', 'Quantum Vault']
cleartext_risk = []
encrypted_gate = []
quantum_vault = []
def passwordstrengthcheck(password):
    score = 0
    # check length
    length = len(user_password)
    if length > 12:
        score += 2
    elif length >= 8 and length <= 12:
        score += 1
    elif length < 8:
        score += 0
    
    #special characters
    specials = "!@#$%^&*()_+{}[]|\\:;\"'<>,.?/~`"

    if any(char in specials for char in user_password):
        score += 1
    else:
        score += 0

    #character cases
    for letter in user_password:
        if letter.islower():
            score += 0
        elif letter.isupper():
            score +=1
    
    #digits
    if any(user_password.isdigit() for user_password in password):
        score += 1

    #usual
    

result= passwordstrengthcheck(user_password)
print(f'pass strength : {result}')
passwordstrengthcheck()
