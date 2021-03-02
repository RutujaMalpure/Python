from Demo1 import *
def main():
    no1=int(input("Enter the first number"))
    no2=int(input("Enter the second number"))

    ret1=Add(no1,no2)
    print("the addition of {} and {} is {} ".format(no1,no2,ret1))

    ret2=Sub(no1,no2)
    print("the Subtration of {} and {} is {} ".format(no1,no2,ret2))

    ret3=Div(no1,no2)
    print("the Division of {} and {} is {} ".format(no1,no2,ret3))

    ret4=Mul(no1,no2)
    print("the Multiplication of {} and {} is {} ".format(no1,no2,ret4))


if __name__=="__main__":
    main()