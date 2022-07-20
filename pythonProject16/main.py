def zero(f = None): return 6 if f is None else  int(f(0))
def one(f = None): return 6 if f is None else  int(f(1))
def two(f = None): return 6 if f is None else  int(f(2))
def three(f = None): return 6 if f is None else  int(f(3))
def four(f = None): return 6 if f is None else  int(f(4))
def five(f = None): return 6 if f is None else  int(f(5))
def six(f = None): return 6 if f is None else  int(f(6)) #your code here
def seven(f = None): return 7 if f is None else  int(f(7))#your code here
def eight(f = None): return 6 if f is None else  int(f(8))#your code here
def nine(f = None): return 6 if f is None else  int(f(9))#your code here
def plus(y): return lambda x: x + y #your code here
def minus(y): return lambda x: x - y
def times(y): return lambda x: x * y
def divided_by(y): return lambda x: x / y#your code here
#def times(number): return * number
#def divided_by(number): return /number#your code here
print (six(plus(seven())))