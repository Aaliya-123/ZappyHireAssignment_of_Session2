number=[]
elements=int(input("Enter the number of elements : "))
print("Enter the elements : ")
for i in range(0,elements):
    i=int(input())
    number.append(i)
print("Odd numbers in the list : ")
for i in range(0,elements):
    if(number[i]%2!=0):
        print(number[i])