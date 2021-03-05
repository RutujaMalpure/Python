"""
.Write a program which accept N numbers from user and store it into List. Return Maximum
number from that List.
Input : Number of elements : 7
Input Elements : 13 5 45 7 4 56 34
Output : 56

"""
def maxnum(arr):

#THIS IS ONE METHOD
    #num=arr[0]     
    #for i in range(len(arr)):
        #if(arr[i]>=num):
            #num=arr[i]
    
    #return num
    
#THIS IS THE SECOND METHOD I.E IN PYTHON    
    num=max(arr)
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

    ret=maxnum(arr)
    print("The max element of list is",ret)

if __name__=="__main__":
    main()