# TaylorHoward
# 10-09-2020
# CIS2348-14654
# Homework #2

# list the months out with the corresponding number
month_list = {"January": "1", "February": "2", "March": "3", "April": "4", "May": "5",
              "June": "6", "July": "7", "August": "8", "September": "9", "October": "10",
              "November": "11", "December": "12"}

# Open the input file that was given with dates
input_file = open('/Users/taylorhoward/UH/CIS2348/InputDates.txt', 'r')


for each in input_file:
    if each != "-1":
        lis = each.split()
        if len(lis) >= 3:
            month = lis[0]
            day = lis[1]
            year = lis[2]

            # How to display the answer with separating with commas or slashes
            if month.lower() in month_list:
                comma = day[-1]
                if comma == ',':
                    day = day[:len(day) - 1]
                    month_number = month_list[month.lower()]
                    ans = month_number + "/" + day + "/" + year



input_file.close()
