"""
Write a program which accept one number and display below pattern.
Input : 5
Output : * * * * *
 * * * * *
 * * * * *
 * * * * *
 * * * * *

"""
def Display(no):
    for i in range(0,no):
        for j in range(0,no):
            print("*",end=" ")
        print("")    
            


def main():
    no=int(input("Enter the number"))
    Display(no)
        
        
if __name__=="__main__":
    main()