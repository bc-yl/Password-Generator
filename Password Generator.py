import re
from dictionary_creation import fill_dict_all, fill_dict_sym
from pass_gen import generate_pass
from parameter_query import check_num, check_symbol
from pass_check import is_valid

val_dict = {}
sym_dict = set()
fill_dict_all(val_dict)
fill_dict_sym(val_dict, sym_dict)
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
while is_valid(password, sym_dict, wants_num, wants_sym) is False:
    password = generate_pass(length, wants_num, wants_sym, val_dict)
org = "Organisation: " + org
usr = "Username: " + usr
password = "Password: " + password
with open("Password Storage.txt", "a") as file:
    file.write(org + "\n")
    file.write(usr + "\n")
    file.write(password + "\n")
    file.write("\n")

