#python challenge
#challenge 0 - 274877906944 in URL

#challenge 1 decipher by adding 2 to the ascii characters.
#def main():
 #   text = input("Enter the text to decipher: \n")
  #  for i in range(len(text)):
   #     if ord(text[i]) >= 97 and ord(text[i]) <= 122:
    #        realc = ord(text[i]) + 2
     #       if realc > 122:
      #          realc = realc - 26
       #     print(chr(realc), end='')
        #else:
         #   print(text[i], end='')
#main()


#challenge 2 view html page source code and find rare characters.
#def main():
 #   with open('pythonchallenge2.txt') as f:
  #      lines = f.readlines()
   #     myDict = {}
    #    for line in lines:
     #       for i in range(len(line)):
      #          if line[i] not in myDict:
       #             myDict[line[i]] = 1
        #        else:
         #           myDict[line[i]] = myDict.get(line[i]) + 1
        #print(myDict)
    #f.close()

#main()


#python challenge equality has to be luuuluuul
def main():
    found = False
    sequence = [None] * 9
    with open('pythonchallenge3.txt') as f:
        txt = f.read().rstrip()
        for i in range(len(txt) - 9):
            for j in range(9):
                sequence[j] = txt[i + j]
            if sequence[0].islower() and sequence[1].isupper() \
            and sequence[2].isupper() and sequence[3].isupper() \
            and sequence[4].islower() and sequence[5].isupper() \
            and sequence[6].isupper() and sequence[7].isupper() \
            and sequence[8].islower():
                found = True
                print(sequence)
            else:
                continue
    if found == False:
        print("End of file, nothing found.")
    f.close()
                
                
                




main()
