"""
Write a program which accept one number form user and return addition of its factors.
Input : 12 Output : 16 (1+2+3+4+6)

"""
def AddFactors(no):
	num=0
	for i in range(1,no):
		if(no%i==0):
			num=num+i
	return num
	
        
def main():
	no=int(input("Enter the number"))
	ret=AddFactors(no)
	print("the adition of factors if {} is {}".format(no,ret))
    
if __name__=="__main__":
    main()