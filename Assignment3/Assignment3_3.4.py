"""
.Write a program which accept N numbers from user and store it into List. Accept one another
number from user and return frequency of that number from List.
Input : Number of elements : 11
Input Elements : 13 5 45 7 4 56 5 34 2 5 65
Element to search : 5
Output : 3


"""
def frequency(arr,no):
    num=0     
    for i in range(len(arr)):
        if(arr[i]==no):
            num=num+1
    
    return num
    

    
def main():
    arr=[]
    print("Enter the number of elements")
    size=int(input())
    
    for i in range(size):
        print("the element at position",i+1)
        no=int(input())
        arr.append(no)
        
    print("the entered list is",arr)
    
    print("Enter the element to be seaarched")
    value=int(input())

    ret=frequency(arr,value)
    print("The frequency of element in the  list is",ret)

if __name__=="__main__":
    main()