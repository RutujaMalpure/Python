"""
Write a program which accept number from user and return number of digits in that number.
Input : 5187934 Output : 7

"""
def DigitCount(no):
	digit=0
	num=0
	while(no!=0):
		num=no%10
		no=no//10
		digit=digit+1
	return digit	

def main():
	no=int(input("Enter the number"))
	ret=DigitCount(no)
	print("The number of digit in {} are {}".format(no,ret))

if __name__=="__main__":
	main()