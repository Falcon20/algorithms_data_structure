def add(x,y):
    while(y!=0):
         carry = x&y
         x= x^y
         y= carry<<1
    return x
    							
print(add(10,22))
#result = 32