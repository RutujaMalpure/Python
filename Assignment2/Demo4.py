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