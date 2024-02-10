input1=input("Enter the string :")
max_freq={}
for i in input1:
    if i in max_freq:
        max_freq[i]=max_freq[i]+1
    else:
        max_freq[i]=1
max1=0
mchar=' '
for i,j in max_freq.items():
    if j>max1:
        max1=j
        mchar=i
print(max_freq)
print(mchar," is the most frequent character.")