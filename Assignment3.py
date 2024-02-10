number=[]
elements=int(input("Enter the number of elements : "))
print("Enter the elements : ")
for i in range(0,elements):
    i=int(input())
    number.append(i)
length=len(number)

print("Sum of Digit in numbers in the list : ")
for i in range(0,elements):
    sum=0
    while(number[i]>0):
        sum+=int(number[i]%10)
        number[i]=number[i]//10
    print(sum,", ")
