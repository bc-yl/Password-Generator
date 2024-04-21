import random

def fill_dict_all(dict: dict) -> dict:
    count = 0
    for n in range(48, 58):  #adds 0-9 to dict
        dict.update({count: chr(n)})
        count += 1
    
    for uc in range(65, 91):  #uc is 10 - 35
        dict.update({count: chr(uc)})
        count += 1
    
    for lc in range(97, 123):  #lc is 36-61
        dict.update({count: chr(lc)})
        count += 1

    for sym_a in range(33, 48):  #symbol is 62-94
        dict.update({count: chr(sym_a)})
        count += 1

    for sym_b in range(58, 65):
        dict.update({count: chr(sym_b)})
        count += 1

    for sym_c in range(91, 97):
        dict.update({count: chr(sym_c)})
        count += 1

    for sym_d in range(123, 127):
        dict.update({count: chr(sym_d)})
        count += 1


    return dict

def generate_pass(length, contains_num, contains_symbol, dict) -> str:
    val_list = []
    if contains_num is False and contains_symbol is False:
        while length > 0:
            val_list.append(dict.get(random.randint(10, 61)))
            length -= 1
    
    if contains_num is True and contains_symbol is False:
        while length > 0:
            val_list.append(dict.get(random.randint(0, 61)))
            length -= 1

    if contains_num is True and contains_symbol is True:
        while length > 0:
            val_list.append(dict.get(random.randint(0, 93)))
            length -= 1
    
    password = ""
    for val in val_list:
        password += val


    return password 

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
length = int(input("Password Length: "))
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

