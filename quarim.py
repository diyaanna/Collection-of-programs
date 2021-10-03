#to find the quotient and remainder od two numbers
def cal(x,y):
    qu = x//y
    print(qu," is the remainder")  
    re = x%y
    print(re," is the remainder")
num1 = int(input("enter the first divident"))
num2 = int(input("enter the first divisor"))
num3 = int(input("enter the second divident"))
num4 = int(input("enter the second divisor"))

print("first set")
cal(num1,num2)

print("Second set")
cal(num3,num4)
