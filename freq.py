#To check the frequency of a character in a list

l = list(input("enter the elements"))
ch = input("enter the element to be checked")
count = 0
for i in range(0,len(l)):
    if ch==l[i]:
        count = count+1
print(ch," comes",count," times in the list")
