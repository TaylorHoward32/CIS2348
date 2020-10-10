#TaylorHoward
#10-05-2020
#CIS2348-14654
#Zylab 6.17

simplepassword=input()
password=''
for x in simplepassword:
    if(x=='i'):
        password+="!"

        #Replace a with @
    elif(x=='a'):
        password+="@"

        #Replace m with M
    elif (x == 'm'):
        password += "M"

        #Replace B with 8
    elif (x == 'B'):
        password += "8"

        #Replace 0 with .
    elif (x == 'o'):
        password += "."

        #As if the password doesn't work
    else:
        password+= x

        #Possibility of adding q*s to the end

password+="q*s"
print(password)

