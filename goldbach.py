num = int(input("integer: "))
counter = 2

while counter <= num:
    #only check even
    if counter % 2 == 0:

        #find the first number
        for first in range(2,counter):
            
            #check if first is a prime
            #how -> iterate through all divisors 2 to first - 1, first % i
            #if isPrime holds True, it is prime
            i = 2
            isPrime = True
            while i < first:
                if first % i == 0 and first > 2: #the 2 case is prime -> skip
                    isPrime = False
                i += 1

            """
                At this point, first has gone through all divisors.
                if first isPrime, then we will check the second num
            """

            if isPrime == True:
                second = counter - first
                if second < 2: #check when second == 1
                    continue

                #check if second isPrime
                j = 2
                while j < second:
                    if second % j == 0 and second > 2:
                        isPrime = False
                    j += 1

            #at this point, first and second have been checked
            if isPrime == True:
                print(counter, '=', first, '+', second)
                break
            
    counter += 1


"""for first in range(2,num):
            
        #check if first is a prime
        #how -> iterate through all divisors 2 to first - 1
        #if isPrime holds True, it is prime
        i = 2
        isPrime = True
        while i < first:
            if first % i == 0 and first > 2:
                isPrime = False
            i += 1
        print(first, isPrime)
"""
