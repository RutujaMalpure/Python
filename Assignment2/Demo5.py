"""
Write a program which accept one number for user and check whether number is prime or not.
Input : 5 Output : It is Prime Number

"""
def Prime(no):
	if (no<=1):
		return False

	for i in range(2,no):
		if(no%i==0):
			return False
	return True		
		

def main():
	no=int(input("Enter the number"))
	ret=Prime(no)
	if(ret==False):
		print("The number {} is not prime".format(no))
	else:
		print("the number {} is prime".format(no))	


if __name__=="__main__":
	main()