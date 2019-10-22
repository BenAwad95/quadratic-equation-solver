#This a script for solve 2nd equation


#import require modules
import  cmath,math,re

# formal of the equation ax^2+bx+c=0
# a cann't be ZERO	



def genral_equ(a,b,c):
	rejex = re.compile(r'(\d.0$)')
	under_root = (b**2)-(4*a*c)
	if under_root < 0:
		state1 = "The roots is complex"
		if rejex.findall(str(math.sqrt(-1 * under_root))) != []:
			state2 = 'Complex root is complate'
			x1 = ((-b) + cmath.sqrt((b**2)-(4*a*c)))/(2*a) 
			x2 = ((-b) - cmath.sqrt((b**2)-(4*a*c)))/(2*a)
		else:
			state2 = 'Complex root is not complete'
			x1 = '(' + str(b) + '+' + str('\u221A%s'% under_root) + ')' + '/%s'% str(2*a)
			x2 = '(' + str(b) + '-' + str('\u221A%s'% under_root) + ')' + '/%s'% str(2*a)
	else:
		state1 = 'The roots is real'
		if  rejex.findall(str(math.sqrt(under_root))) != []:
			state2 = 'The root is complete'
			x1 = ((-b) + math.sqrt((b**2)-(4*a*c)))/(2*a)
			x2 = ((-b) - math.sqrt((b**2)-(4*a*c)))/(2*a)
		else:
			state2 = 'The root is not complete'
			x1 = '(' + str(b) + '+' + str('\u221A%s'% under_root) + ')' + '/%s'% str(2*a)
			x2 = '(' + str(b) + '-' + str('\u221A%s'% under_root) + ')' + '/%s'% str(2*a)
	anaswer = '%s\nRoot1 = %s\nRoot2 = %s'%(state1,x1,x2)
	return anaswer

def input_values():
	print ('Hello, I\'m quadratic equations\' solver\nEnter a,b and c values down below.')
	a = 0
	while a == 0:
		a = int(input ('a = '))
		if a == 0:
			print ('a Cann\'t be zero\nPlease try again')
			continue
		b = int(input ('b = '))
		c = int(input ('c = '))
	print (genral_equ(a,b,c))

input_values()