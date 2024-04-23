#A smart parking lot displays different messages to the visitor based on the number of available spaces.
#Task
#Complete the program to inform the user about available spaces in the parking lot
'''
spaces = int(input())

while spaces > 0:
    print("Available Spaces "+ str(spaces))
    spaces = spaces - 1

print("Sorry, the parking lot is full") 

#=======================================================================================================

spaces = int(input())

if spaces > 0:
    print("Available spaces")
else:
    print("Sorry, the parking lot is full")
'''
#2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
#You are developing software for a medical device that informs patients about their blood sugar level.
#Task
#Complete the given code to display different messages to the patient based on the blood sugar levels
'''
glucose_level = int(input())

if glucose_level == 60:
    print("Low glucose level")
elif glucose_level == 100:
    print("Normal range")
elif glucose_level == 150:
    print("High glucose level")
'''

#3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
#Imagine you are a scientist looking at a new type of cell under the microscope. This type of cell 
#divides itself into 2 daughter cells every 24 hours, meaning that the cell population duplicates every day.
#Task
#Complete the code to take the initial cell population and the number of days you are observing the
#cells to calculate the cell population at the end of each day in the following format

