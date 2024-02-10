number=[]
elements=int(input("Enter the number of elements : "))
print("Enter the elements : ")
for i in range(0,elements):
    i=int(input())
    number.append(i)
l=len(number)
first=number[0]
for i in range(0,l):
    if(number[i]>first):
        first=number[i]
print("Largest Element in array = ",first)     