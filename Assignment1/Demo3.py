"""
Write a program which contains one function named as Add() which accepts two numbers
from user and return addition of that two numbers.
Input : 11 5 Output : 16

"""
def Add(no1,no2):
    ans=no1+no2
    return ans    
    
def main():
    no1=int(input("Enter the first number"))
    no2=int(input("Enter the second number"))
    ret=Add(no1,no2)
    print("The addition of {} and {} is {}".format(no1,no2,ret))
        
if __name__=="__main__":
    main()