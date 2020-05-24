c = input('Enter temp in Celsius:')
try:
    f = 32 + 9/5*float(c)
    print('Temp in Fahrenhite :',f)
except:
	print('Please Enter a Number!')	
