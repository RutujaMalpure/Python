"""
. Write a program which accept number from user and print that number of “*” on screen.
Input : 5 Output : * * * * *

"""
def Display(no):
	for i in range(0,no):
		print("*")
		
def main():
	no=int(input("Enter the number"))
	Display(no)
if __name__=="__main__":
	main()