#write  a program that prints the squares of all integers from 1 to 10 using a for loop.
i = 1
while(i<=10):
    j = i*i
    print(" ",i,"= ",j)
    i =i+1


#write a programs that checks if a given number is between 10 and 20 is also inclusive using logical operators.
a = 10
b = 20

print((a < 15) and (b <= 20))
print((a < 5) or (b < 6))
    

#write a program that converts the temperature of fahrenheit,to celsiius degrees the program should ask the user to enter the temperature in celsius degrees and then display the temperature converted to fahreinheit degrees
#include<studio.h>


celsius_temperature= float(input("enter the temperature value in celsius: "))
fahrenhet_temperature =(celsius_temperature *1.8) +32
print(f"the temperature in degrees fahrenhet is: {fahrenhet_temperature}")
     
            

     

#formula is mpg/miles driven /gallons of gas used. write a program that asks the user for the number of miles driven and gallons used.
#it should calculate the cars miles per gallons used and display the results.

milesdriven = float(input("enter the number of milesdriven: "))
gallonofgasused = float(input("enter the gallonsof gas used: "))
milespergallon = milesdriven / gallonofgasused
print("the cars miles _per_gallon is " + milespergallon) 


#n0 5
student_name = input("Enter the student_name: ")
student_number= input("Enter the student_number: ")
programming = input( "Enter the programming mark: ")
data_science = input(" Enter the data_science mark: ")
computer_application = (" Enter the computer_application mark: ")
sum = programming + data_science + computer_application
total_subject = 3
average = round(sum/total_subject,3)
print ( f"the average of {student_name} and numberis: {student_number} is: {average:.3f}")
