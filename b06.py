
def func3(x, y, z):
	res = y + z - x
	if (res < 0):
		res = res * -1
	return res

def func2(y, z):
	res = (2 * z) + y - 5
	return res

def func1(x):
	res = 2 * x + 11
	return res



def solver(sym1, sym2, sym3):
	symbols = {"0nnnnn" : 0, "n01nnn" : 11, "n1n0nn" : 10, "1001nn" : 22, "0110nn" : 21, "n011n0" : 20}
	xval = symbols[sym1]
	yval = symbols[sym2]
	zval = symbols[sym3]
	
	return func1(xval), func2(yval, zval), func3(xval, yval, zval)

print(solver(input("x:"), input("y:"), input("z:")))  
