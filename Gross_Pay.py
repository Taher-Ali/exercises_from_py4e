h = input('Enter Hours:')
r = input('Enter Rate:')
try:
	if float(h) > 40:
		p = 1.5*float(h)*float(r)
	else:
		p = float(h)*float(r)
	print('Gross Pay:',p)
except: 
	print('Please Enter a Number!')	
