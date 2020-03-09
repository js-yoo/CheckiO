# https://py.checkio.org/en/mission/house-password/
# Difficulty : Simple

def checkio(data:str)->bool:
    con1=all(char.isalnum() for char in data)
    con2=any(char.islower() for char in data)
    con3=any(char.isupper() for char in data)
    con4=any(char.isdigit() for char in data)
    
    if len(data)<10:
        return False
    elif con1 and con2 and con3 and con4:
        return True
    else:
        return False
    
    
# Example)
# checkio('A1213pokl') == False
# checkio('bAse730onE') == True
# checkio('asasasasasasasaas') == False
# checkio('QWERTYqwerty') == False
# checkio('123456123456') == False
# checkio('QwErTy911poqqqq') == True
