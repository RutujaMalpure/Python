"""
. Write a program which accept one number and display below pattern.
Input : 5
Output : * * * * *
 * * * *
 * * *
 * *
 *

"""
def DisplayPattern(no):
	if(no<0):
		no=-no

	for i in range(0,no):
		for j in range(0,no):
			print("*",end=" ")
		print("")		
		no=no-1
	
	
    
def main():
	no=int(input("Enter the number"))
	DisplayPattern(no)


if __name__=="__main__":
	main()