def sortLen(*args):
    sortedList= []
    
    listargs = list(args)
    while (len(listargs) > 0):
        mins = listargs[0]
        
        for i in range(len(listargs)):
            if len(listargs[i]) < len(mins):
                mins = listargs[i]
                
        sortedList.append(mins)
        listargs.remove(mins)

    return sortedList

def main():
    print(sortLen('lychee', 'pineapple', 'mango'))

main()
