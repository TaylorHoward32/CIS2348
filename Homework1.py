#Taylor Howard
#September 12, 2020
#CIS2348 Python
#AmauryLendasse

#Stating the Title of the Code/ Purpose
print('Birthday Calculator, (input whole numbers for each response)')

#Have the user input the Current Month.
month1 = int(input('What is the current Month?: '))

#Have the user input the Current Day.
day1= int(input('What is the current Day?: '))

#Have the user input the Current Year.
year1 = int(input('What is the current Year: '))

print('Birthday')
#Have User input their birthday month.
month2 = int(input('What is your Birthday Month?: '))

#Have user input their birthday date.
day2 = int(input('What is your Birthday Date: '))

#Have user input their birthday year.
year2 = int(input('What is your Birthday Year?: '))

#Subtracting the years from each other.
years = year1-year2-1

#What If statements to prompt the birthday is current or the age!
if(month2<month1):
    years+=1
elif(month1==month2):
    if(day2<day1):
        years+=1
if (month1==month2 and day1==day2):#printing happy Birthday if current day is his birthday
    print('Happy Birthay')
print('You are '+str(years)+" years old.")