# length, special character, uppercase lowercase, digits, (root, admin, god)
import time
import sys

#CLEARTEXT RISK, ENCRYPTED GATE, QUANTUM VAULT
# def welcomemessage(text, delay=0.07):
#     for character in text:
#         sys.stdout.write(character)
#         sys.stdout.flush()
#         time.sleep(delay)
#     print()
# welcomemess= "    Welcome to Topiary's Password Strength Analyzer    "
# welcomemessage(welcomemess, delay=0.07)

def proceed(text, delay = 0.06):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)
    print
question = input('Do you want to you to use the program? (y/n): ')
if question == 'y':
    
        user_password = (input('Input password to test: '))
        strength_label = ['ClearText Risk', 'Encrypted Gate', 'Quantum Vault']

        
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
        usual = ['root', 'admin',' god', 'master', '123456', '12345', 'guest', 'secret', 'qwerty'] 
        if user_password in usual:
                    score += 0
        elif user_password not in usual:
                    score +=1

        if score >= 6:
                    print(strength_label[2])
        elif score >= 3:
                    print(strength_label[1])
        elif score < 3:
                    print(strength_label[0])
        result= (user_password)
        print(f'Your password strength is : {result}')


proceed(question, delay = 0.06)
