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

def fill_dict_sym(val_dict: dict, sym_dict: dict):
    for index in range(62, 94):
        sym_dict.add(val_dict.get(index))
    
    return sym_dict
