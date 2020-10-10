#TaylorHoward
#10-05-2020
#CIS2348-14654
#Zylab 8.10

word=input()
word.replace(" ","")
length=len(word)
def palindrome(li):
    flag=0
    mid=length/2
    i=0
    while(i<mid+1):
        if(li[i]!=li[length-i-1]):
            flag=1
            break
        else:
            i=i+1

    if(flag==1):
            print(li,"is not a palindrome")
    else:
            print(li,"is a palindrome")
palindrome(word)
