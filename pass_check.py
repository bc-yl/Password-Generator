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