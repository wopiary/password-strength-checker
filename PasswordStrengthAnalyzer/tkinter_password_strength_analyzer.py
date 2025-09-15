import tkinter as tk
import os
from PIL import ImageTk, Image
os.system('cls' if os.name=='nt' else 'clear')
win = tk.Tk()
win.geometry('325x125')
win.title('Password Strength Analyzer')



title_label = tk.Label(win, text='Analyze Password Strength', font=('MS Sans Serif', 16))
title_label.pack(pady=5)



heading_label = tk.Label(win, text='Rating:', font=('MS Sans Serif', 10, 'bold'))
heading_label.pack()

rating_result_var = tk.StringVar()
rating_result = tk.Label(win, textvariable=rating_result_var, text='_____________')
rating_result.pack()

frame = tk.Frame(win)
frame.pack(side=tk.TOP)

img = 'ye-removebg-preview.png'
if os.path.exists(img):

        icon_image =ImageTk.PhotoImage(Image.open("ye-removebg-preview.png"))
        icon_img_beside_label = tk.Label(frame, image=icon_image)
        icon_img_beside_label.pack(side=tk.LEFT)


else: 
        pass
enter_pass_label = tk.Label(frame, text='E̲nter password:', font=('MS Sans Serif', 4))
enter_pass_label.pack(side=tk.LEFT)

input_password_var = tk.StringVar()
input_password = tk.Entry(frame, textvariable=input_password_var)
input_password.pack(side=tk.LEFT,pady=2)

strength_label = ['[Low] ClearText Risk', '[Fair] Encrypted Gate', '[Strong] Quantum Vault']
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
                    if input_password_var in usual:
                                    score -= 2
                    elif input_password_var not in usual:
                                    score +=1

                    if score >= 6:
                                    return strength_label[2]
                    elif score >= 4:
                                    return strength_label[1]
                    elif score <4:
                                    return strength_label[0 ]


test_button = tk.Button(frame, text='Run', font=('MS Sans Serif', 4))
test_button.pack(side=tk.LEFT, padx=10)
test_button.bind('<Button-1>', lambda event: rating_result_var.set(passwordstrengthcheck(input_password_var.get())))

clear_button = tk.Button(frame, text='Del', font=('MS Sans Serif', 4))
clear_button.pack(side=tk.LEFT)
clear_button.bind('<Button-1>', lambda event: (rating_result_var.set(' '), input_password.delete(0, tk.END)))
win.mainloop()