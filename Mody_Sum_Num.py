#Ali Mody
#This program will output the sum of positive numbers that are entered.

#Initialize Vairables

total_sum = 0
number = 0

#The Loop that will process the positive numbers

while number >=0 :
    total_sum += number
    number = int(input("Please input the positive numbers. "))

#Shows the out of the sum of all the numbers
print("The total sum of all the positive numbers is", total_sum)
