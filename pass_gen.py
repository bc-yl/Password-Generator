import random

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