"""
. Write a program which contains one function that accept one number from user and returns
true if number is divisible by 5 otherwise return false.
Input : 8 Output : False
Input : 25 Output : True

"""
def Divisible(no):
	if no % 5==0:
		return True
	else:
		return False

def main():
	no=int(input("enter the number"))
	ret=Divisible(no)
	if(ret==True):
		print("{} is divisble ".format(no))
	else:
		print("{} is not divisble".format(no))
if __name__=="__main__":
	main()