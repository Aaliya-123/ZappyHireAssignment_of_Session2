word=input("Enter a word:")
last=len(word)-1
first=0
count=0
while(first<last):
    if(word[last]==word[first]):
        count=count+1
    first=first+1
    llast=last-1
if(count!=0):
    print(word," is palindrome.")
else:
    print(word," is not palindrome.")