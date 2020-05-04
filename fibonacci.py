'''
Program to find the nth Fibonacci number
'''

def Fibonacci(n):
    '''
    Function for nth Fibonacci number
    '''
	if n<0:
		print("Incorrect input")
	# First Fibonacci number is 0
	elif n==1:
		return 0
	# Second Fibonacci number is 1
	elif n==2:
		return 1
	else:
		return Fibonacci(n-1)+Fibonacci(n-2)

if __name__ == '__main__':
    
    # input a number from user
    number = input("Enter a number:")

    #find the nth fibonacci number
    fibo = Fibonacci(number)

    #print the number
    print("The fibonacci number is:", fibo)
