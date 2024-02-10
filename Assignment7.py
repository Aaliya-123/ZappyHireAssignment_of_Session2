word=input("Enter the word : ")
l1=[]
for i in word:
    if i!='a' and i!='e' and i!='i' and i!='o' and i!='u':
        l1.append(i)
str_l1=''.join(l1)
print("Without vowel = ",str_l1)