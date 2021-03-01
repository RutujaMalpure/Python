def digitAdd(no):
	digit=0
	num=0
	while(no!=0):
		num=no%10
		no=no//10
		digit=digit+num
	return digit	

def main():
	no=int(input("Enter the number"))
	ret=digitAdd(no)
	print("The addition of digit is {}".format(ret))

if __name__=="__main__":
	main()