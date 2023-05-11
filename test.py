"""
class ListNode(object): #we pass an array object into the class ListNode
    #this __init__ line also tells us which parameter comes first
    def __init__(self, val=0, next=None): #if no parameter, set the val of
        #itself to 0 and next to None
        self.val = val #set .val of instance to the first parameter given
        self.next = next #set .next to the next item in the array

        
integer = 2
point1 = ListNode(3, integer)

print(point1, point1.val, point1.next)

point1 = point1.next

print(point1)


"""








"""
l1 = ListNode([2,4,2,3,6,8])
l2 = ListNode([5,6,6])
#output should be [7, 0, 0, 1]


total = l1


i = 0
carry = False
if len(total.val) < len(l2.val):
    initial_len = len(l2.val)
    total = l2
else:
    initial_len = len(total.val)
    total = l1
    
while i < initial_len:
    try:
        total.val[i] += l2.val[i]
    except IndexError:
        total.val[i] += 0
    if carry == True:
        total.val[i] += 1
        carry = False
    if total.val[i] > 9:
        carry = True
        total.val[i] -= 10
        if total.val[i + 1] != None: #check if there is something after i
            print("There is something at", i + 1)
        else: #if null after i, then carry over the 1
            total.val.append(1)
    i += 1
        


print(total.val)
"""


def findmax():
    list1 = [1, 2, 3, 10, 5, 8]
    N = 66
    length = len(list1)

    sums = 0;
    counter = 0;

    while (sums <= N and counter < length):
        sums += list1[counter]
        counter += 1

    if sums > N:
        return counter - 1
    return counter

#check longest -> if is palindrome, no need to check further
#if not palindrome, check other substring with same length

def palindrome(s):
    longestpal = ''
    for i in range(len(s)):
        for j in range(len(s)):
            teststring = s[i: j + 1]
            palindrome = True
            for index in range(len(teststring)):
                if teststring[index] != teststring[-(index + 1)]:
                    palindrome = False
                    break
            if palindrome == True:
                if len(teststring) > len(longestpal):
                    longestpal = teststring
    return longestpal

def isPalindrome(s):
    for index in range(len(s) // 2 + 1):
        if s[index] != s[-(index + 1)]:
            return False
    return True


def betterpalindrome(s):
    length = len(s)
        iteration = 0
        while iteration < length:
            for i in range(iteration + 1):
                if isPalindrome(s[0 + i: len(s) + i - iteration]):
                    return s[0 + i: len(s) + i - iteration]
            iteration += 1



print(betterpalindrome("babad"))

def reversed(s):
    reverse = ''
    for index in range(len(s)):
        reverse += s[-(index + 1)]

    longest = []
    palindrome = ''

    for index in range(len(s)):
        if reverse[index] == palindrome


