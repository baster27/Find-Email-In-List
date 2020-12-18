import time
from random import choice
from string import ascii_lowercase as letters

def binarySearch_iter(n,arr):
    '''This is an iterative approach'''
    start = 0
    stop = len(arr) - 1
    while start <= stop:
        mid = (start + stop) // 2
        if n == arr[mid]:
            return mid, f"{n} found at index: {mid}"
        elif n > arr[mid]:
            start = mid + 1
        else:
            stop = mid - 1
    return None, f"{n} not found in list"

def analyze(funcName, *args):
    startTime = time.time()
    funcName(*args)
    endTime = time.time()
    seconds = endTime - startTime
    print(f"{funcName.__name__.capitalize()}\t-> Elapsed time: {seconds:.5f}")

##### Functions to generate lists of random emails #####
def generateName(lengthOfName):
    return ''.join(choice(letters) for i in range(lengthOfName))

def getDomain(listOfDomains):
    return choice(listOfDomains)

def generateEmails(lengthOfName, listOfDomains, totalEmails):
    emails = []
    for num in range(totalEmails):
        emails.append(generateName(lengthOfName)+"@"+getDomain(listOfDomains))
    return emails
