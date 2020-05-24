g = input('Enter your Score :')
try:
 	if float(g) > 1.0 :
 		print('Enter a valid Score')
 	elif float(g) >= 0.9 :
 		print('A')
 	elif float(g) >= 0.8 :
 		print('B')
 	elif float(g) >= 0.7 :
 		print('C')
 	elif float(g) >= 0.6 :
 		print('D')
 	elif float(g) < 0.6 :
 		print('F')
 	
except :
	print('Hey oversmart! Enter a Number!')
				
