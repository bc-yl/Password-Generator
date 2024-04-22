import random
import re
from dictionary_creation import fill_dict_all
from pass_gen import generate_pass


def check_symbol() -> bool:
    response = input("Contains symbols (Y/N): ")
    if response == "Y" or response == "y":
        return True


    return False

def check_num() -> bool:
    response = input("Contains numbers (Y/N): ")
    if response == "Y" or response == "y":
        return True
    

    return False

def contains_sym(password: str, sym_dict):
    for val in range(len(password)):
        if password[val] in sym_dict:
            return True
    

    return False

def contains_num(password: str):
    for val in range(len(password)):
        if password[val].isdigit():
            return True
        
    
    return False

def contains_uc(password: str):
    for val in range(len(password)):
        if password[val].isupper():
            return True
        
    
    return False

def contains_lc(password: str):
    for val in range(len(password)):
        if password[val].islower():
            return True
        
    
    return False

val_dict = {}
sym_dict = set()
fill_dict_all(val_dict)
for index in range(62, 94):
    sym_dict.add(val_dict.get(index))
org = input("Organisation: ")
usr = input("Username: ")
while True:
    length = input("Password Length (8+): ")
    if not re.match("^[0-9]+$", length):
        print("Please enter a valid number!")
        continue
    if int(length) < 8:
        print("Please enter a number greater than 7!")
    else:
        length = int(length)
        break
wants_num = check_num()
wants_sym = False
if wants_num:
    wants_sym = check_symbol()
password = generate_pass(length, wants_num, wants_sym, val_dict)
while (contains_lc(password) == False or contains_uc(password) == False or
       contains_num(password) != wants_num or contains_sym(password, sym_dict) 
       != wants_sym):
    password = generate_pass(length, wants_num, wants_sym, val_dict)
org = "Organisation: " + org
usr = "Username: " + usr
password = "Password: " + password
with open("Password Storage.txt", "a") as file:
    file.write(org + "\n")
    file.write(usr + "\n")
    file.write(password + "\n")
    file.write("\n")

