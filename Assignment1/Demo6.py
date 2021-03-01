"""
Write a program which accept number from user and check whether that number is positive or
negative or zero.
Input : 11 Output : Positive Number
Input : -8 Output : Negative Number
Input : 0 Output : Zero

"""
def ChkNum(no):
	if no==0:
		return
	elif no>0:
		return True
	else:
		return False
    
def main():
	no=int(input("Enter the number"))
	ret=ChkNum(no)
	if  ret==True:
		print("{} is Positive Number".format(no))
	elif ret==False:
		print("{} is Negative Number".format(no))
	else:
		print("the {} is zero number".format(no))


if __name__=="__main__":
	main()