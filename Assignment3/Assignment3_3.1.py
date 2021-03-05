"""
Write a program which accept N numbers from user and store it into List. Return addition of all
elements from that List.
Input : Number of elements : 6
Input Elements : 13 5 45 7 4 56
Output : 130

"""
def Add(arr):
    sum=0
    for i in range(len(arr)):
        sum=sum+arr[i]
        
    return sum

def main():
    arr=[]
    print("Enter the number of elements")
    size=int(input())
    
    for i in range(size):
        print("the element at position",i+1)
        no=int(input())
        arr.append(no)
        
    print("the entered list is",arr)

    ret=Add(arr)
    print("The addition of all element of list are",ret)

if __name__=="__main__":
    main()