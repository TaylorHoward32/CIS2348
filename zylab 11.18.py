#Taylor Howard
#11-01-2020
#CIS2348-14654
#Zylab 11.18

#user enter numbers on single line
num_values = input()
# convert values to integers that are greater than zero
list_values = [int(num) for num in num_values.split()
               if int(num) >= 0]
#values in ascending order
list_values.sort()
 #display only positive integers w/ spaces
for value in list_values:
    print(value, )

