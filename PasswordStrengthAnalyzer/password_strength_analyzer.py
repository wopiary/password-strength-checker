# length, special character, uppercase lowercase, digits, (root, admin, god)
import time
import sys
import keyboard
import os 
import tkinter as tk

os.system('cls' if os.name == 'nt' else 'clear')
def welcomemessage(text, delay=0.07):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)
    print()
welcomemess= "    Welcome to Topiary's Password Strength Analyzer    "
welcomemessage(welcomemess, delay=0.07)

def animated_input(prompt, delay =0.04):
        for char in prompt:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(delay)
        return input()

question = animated_input("Do you want to you to use the program? (y/n): ")
if question == 'y':
        
        user_password = (input(' Input password to test: '))
        strength_label = ['ClearText Risk', 'Encrypted Gate', 'Quantum Vault']
        def passwordstrengthcheck(password):
                
                
                
                score = 0


                        # check length
                length = len(password)
                if length > 12:
                                score += 2
                elif length >= 8 and length <= 12:
                                score += 1
                elif length < 8:
                                score += 0
                        

                        #special characters
                specials = "!@#$%^&*()_+{}[]|\\:;\"'<>,.?/~`"

                if any(char in specials for char in password):
                                score += 1
                        

                        #character cases
                has_lower = any(char.islower() for char in password)
                has_upper = any(char.isupper() for char in password)

                if has_lower and has_upper:
                        score += 2
                elif has_lower or has_upper:
                        score += 1
                else:
                        score += 0

                        #digits
                if any(user_password.isdigit() for user_password in password):
                                score += 1


                        #usual
                usual = ['root', 'admin',' god', 'master', '123456', '12345', 'guest', 'secret', 'qwerty'] 
                if user_password in usual:
                                score -= 2
                elif user_password not in usual:
                                score +=1

                if score >= 6:
                                return strength_label[2]
                elif score >= 4:
                                return strength_label[1]
                elif score <4:
                                return strength_label[0]
                
        result= passwordstrengthcheck(user_password)
        print(f'\nYour password strength is : {result}\n')
elif question == 'n':
        del()
else:
        print('\nCommand Unavailable!\n')
