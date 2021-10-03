# find largest number from the list
list1 = []
  

num = int(input("Enter numbers : "))
  
for i in range(1, num + 1):
    ele = int(input("Enter elements: "))
    list1.append(ele)
      

print("Largest element is:", max(list1))
