def is_valid(password: str, sym_dict: set, wants_num: bool, wants_sym: bool):
    contains_sym = False
    contains_lc = False
    contains_uc = False
    contains_num = False
    for val in range(len(password)):
        if (contains_sym == wants_sym and contains_lc is True and contains_num
            == wants_num and contains_uc is True):
            return True
        elif password[val] in sym_dict:
            contains_sym = True
            continue
        elif password[val].isupper() is True:
            contains_uc = True
            continue
        elif password[val].islower() is True:
            contains_lc = True
            continue
        elif password[val].isdigit() is True:
            contains_num = True
            continue
    

    return False

