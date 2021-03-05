"""
Write a program which accept N numbers from user and store it into List. Return addition of all
prime numbers from that List. Main python file accepts N numbers from user and pass each
number to ChkPrime() function which is part of our user defined module named as
MarvellousNum. Name of the function from main python file should be ListPrime().
Input : Number of elements : 11
Input Elements : 13 5 45 7 4 56 10 34 2 5 8
Output : 54 (13 + 5 + 7 +2 + 5)




"""
from MarvellousNum import *

def ListPrime(arr):
    Sum=0
    for num in arr:
        Sum=Sum+num
    return Sum    

def main():
    arr=[]
    print("Enter the number of elements")
    size=int(input())
    
    for i in range(size):
        print("the element at position",i+1)
        no=int(input())
        arr.append(no)
        
    print("the entered list is",arr)
    
    ret=list(filter(ChkPrime,arr))
    print("the prime numbers from the list are",ret)
    
    ret1=ListPrime(ret)
    print("Addition of all prime numbers is",ret1)
    

if __name__=="__main__":
    main()