def dfiveorsev(a):
  if (a%5==0) and (a%7==0):
    print("Divisible by 5 and 7")
  else:
    print("It is not divisible")

a=int(input("Enter a number : "))
dfiveorsev(a)
