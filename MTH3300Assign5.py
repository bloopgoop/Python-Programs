def tenth(sentence):
    word = 0
    tenth = ""
    for char in sentence:
        if char == ' ':
            word += 1
        if word == 9 and char != ' ':
            tenth += char
    return tenth
            

    
print(tenth("one two thee four five six seven eight nine ten eleven"))

def decrypt(sentence):
    for char in sentence:
        if char != 'e' and char != 'w' and char != 'l':
            num = pow(ord(char), 19) % 201
            print(chr(num), end='')
        else:
            print(char, end='')
    print('')
            
            
decrypt("Di¾ÅÇuÅY°uw¥Å6u:a­uevÅha²eÅ:u]eÅde°evÅ­ha°Åh:a°v¦")
decrypt("h:a°vÅvha]eÅ3%ÅuÅ­hei]ÅDWÅwi­hÅBa°a°av¦")


def passesConditions(password):
    if len(password) < 6:
        return False
    hasLower = False
    hasUpper = False
    digits = 0
    hasSymbol = False
    for char in password:
        if char.islower():
            hasLower = True
        if char.isupper():
            hasUpper = True
        if char == '$':
            hasSymbol = True
        if char.isdigit():
            digits += 1
    
    if hasLower and hasUpper and digits <= 3 and hasSymbol == False:
        print("password accepted")
        return True
    else:
        return False
        
def askPassword():
    password = input("Enter a password: ")
    while passesConditions(password) == False:
        password = input("Enter a password: ")
        
askPassword()