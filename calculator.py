#Calculator program

#process_numbers() method performs arithmetic 
#operations (add, subs, multi, div) when it is called
def process_numbers(numbers):
    #menu bar for operations
    if numbers:
        print('Choose the operation: ')
        print('1. Addition')
        print('2. Substraction')
        print('3. Multiplication')
        print('4. Division')
    
        choice = int(input('Enter your choice: '))
        #operation is performed according to the chosen option from menu
        if choice == 1:
            result = sum(numbers)
            op = 'Addition'
        elif choice == 2:
            result = numbers[0]
            for num in numbers[1:]:
                result -= num
            op = 'Subtraction'
        elif choice == 3:
            result = numbers[0]
            for num in numbers[1:]:
                result *= num
                op = 'Multiplication'
        elif choice == 4:
            result = numbers[0]
            try:
                for num in numbers[1:]: 
                    result /= num
                    op = 'Division'
            except ZeroDivisionError:
                result = 'ZeroDivisioError'
                op = 'Division'
            else:
                print('Division successful!')
        else:
            print('Invalid choice!!!')
    
        return op, result

#number of input numbers is taken from user
n = int(input('Enter number of inputs: '))
#an empty numbers_list[] is created
numbers_list = []
#Each number is then taken from user input
if n:
    for i in range(1,n+1):
        nn= int(input('Enter number {}: '.format(i)))
        numbers_list.append(nn)
else:
    print('There are zero input numbers')
    n = int(input('Please enter number of inputs: '))
    for i in range(1,n+1):
        nn= int(input('Enter number {}: '.format(i)))
        numbers_list.append(nn)


print(numbers_list)  
#process_numbers() method is called where numbers_list[] is passed as an agrument
operation, result = process_numbers(numbers_list)
#the return from the method is saved into the variables operation and result and printed on user console
print('The {} of numbers {} is {} '.format(operation,numbers_list,result))