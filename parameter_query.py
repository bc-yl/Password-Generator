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