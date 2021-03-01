"""
. Write a program which accept name from user and display length of its name.
Input : Marvellous Output : 10

"""
def DisplayLength(name):
	ans=len(name)
	return ans
def main():
	name=input("Enter the name")
	ret=DisplayLength(name)
	print("the length of {} is {}".format(name,ret))
	
if __name__=="__main__":
	main()