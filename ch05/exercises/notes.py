def foo(x,y,z):
    print(x,y,z)
foo(1,2,3)
#local scope variable gets deleted when the function ends
def foos():
    local_var = 5 
    x = 2 
def fooos():
    local_var = 8 
def fosball():
    x= 5 
    return x
y = fosball() 
print (y)
print(fosball())
def myfunc(x = 0):
    return x +x
myfunc(5)
def power(x=0,p=0):
    power = p 
    y = x** power 
    return y 
power = 2 
result = power(5,3)
print(result )