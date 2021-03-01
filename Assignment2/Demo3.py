def Fact(no):
    num=1
    while(no!=0):
        num=num*no
        no=no-1
    return num
    
def main():
    no=int(input("Enter the first number"))
    ret=Fact(no)
    print("the Factorial of {} is {}".format(no,ret))
    
        
if __name__=="__main__":
    main()