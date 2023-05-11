def main():
    word = input("Enter a word\n")
    length = len(word)

    for i in range(length):
        print(replace(word[i]), end='')

    print("\n")





def replace(character):
    if character.upper() == 'A':
        return '6'
    elif character.upper() == 'I':
        return '1'
    elif character.upper() == 'O':
        return '0'
    elif character.upper() == 'E':
        return '3'
    else:
        return character


main()
