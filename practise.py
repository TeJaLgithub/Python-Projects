#n = int(input("Enter integer: "))
#CODE1
'''
n = 1
if 1 <= n <= 100:
    if n % 2 != 0:
        print("Weird")
        print("loop 1")
    elif n % 2 == 0 :
        if 2 <= n <= 5:
            print("Not Weird")
            print("loop 2")
        if 6 <= n <= 20:
            print("Weird")
            print("loop 3")
        if n > 20:
            print("Not Weird")
            print("loop 4")

n = int(input("enter n: "))
if 1 <= n <= 20:
    for i in range(0,n,2):
     print(i**2)
'''
#CODE 2
'''
def is_leap(year):
    leap = False
    
    # Write your logic here
    if 1900 <= year <= 10**5:
        if year % 4 == 0:
            leap = True
        elif year % 100 == 0 and year % 400 == 0:
            leap = True
        else:
            leap = False
    
    return leap

year = int(input("input year: "))
print(is_leap(year))
'''

#CODE3
'''
n = int(input("Enter integer: "))
if 1 <= n <= 150:
    for i in range(1,n+1):
        print(i, end = " ")
'''

#CODE4
'''
if 1 <= n <= 99:
    v = n-(2**x)
    if 
        for i in range(1,n+1):

            print(i, a,end =" ")
x=0
for i in reversed(range (n)):
    power2 = 2**x
    while power2 < n:
        result = list (map (lambda x: 2 ** x, range (n)))
        x +=1
        power2 = 2**x
        print (result [i],end=" ")

print ('The total number of terms are:', n)

for i in reversed(range (n)):

              #print ('2 raised to the power', i, 'is', result [i])
              print (result [i],end=" ")
'''
'''
while n:
     print("")
     print("1)Decimal")
     print("2)Binary")
     print("3)Hexadecimal")
     print("4)Octal")
     print("")
     choice = int(input("Enter your choice: "))
     print("-----------------------------------")
     print("")


     if 1 <= n <= 99:
        if choice == 1:
            print("Decimal of integer ",n," is ",n)
        elif choice == 2:
            #BINARY
            binary=''
            x = n
            while x > 0:
                remainder1 = x % 2
                binary = str(remainder1) + binary
                x //= 2
            print("Binary of integer ",n," is ",binary)
        elif choice == 3:
            #Hexadecimal
            decimal_to_hex = [i if i < 10 else hex(i)[2:].upper() for i in range(16)]
            
            r = []
            x = n
            while x!=0: 
                quotient2 = x//16 #quo=15
                remainder3 = x%16 #Remain=13
                r.append(decimal_to_hex[remainder3]) #r = [5]
                x = quotient2
        
            o = ''.join(map(str, reversed(r)))
            print("Hex of integer ",n," is ",o)
        elif choice == 4:
            #Octal
            r = []
            x = n
            while x!=0: 
                quotient1 = x//8 #quo=31
                remainder2 = x%8 #Remain=5
                r.append(remainder2) #r = [5]
                x = quotient1

                o = int(''.join(map(str, reversed(r))))
            print("Octal of integer ",n," is ",o)
        else:
            print("invalid choice!!!")
            break
        '''
'''
for i in range(1,n+1):
    # Decimal representation
    decimal_result = str(i)

    # Octal representation
    r_octal = []
    x_octal = i
    while x_octal != 0:
        quotient_octal = x_octal // 8
        remainder_octal = x_octal % 8
        r_octal.append(str(remainder_octal))
        x_octal = quotient_octal
    octal_result = ''.join(reversed(r_octal)).rjust(3,' ')

    # Hexadecimal representation
    decimal_to_hex = [j if j < 10 else hex(j)[2:].upper() for j in range(16)]
    r_hex = []
    x_hex = i
    while x_hex != 0:
        quotient_hex = x_hex // 16
        remainder_hex = x_hex % 16
        r_hex.append(decimal_to_hex[remainder_hex])
        x_hex = quotient_hex

    hex_result = ''.join(map(str, reversed(r_hex))).rjust(4, ' ')

    # Binary representation
    binary = ''
    x = i
    while x > 0:
        remainder = x % 2
        binary = str(remainder) + binary
        x //= 2
    binary_result = binary.rjust(4, ' ') 

    print(f"{decimal_result:>4}{binary_result:>6}{octal_result:>5}{hex_result:>5}")
'''        

#pattern making
'''
def print_formatted(number):
    # your code goes here
    if 1 <= n <= 99:
        for i in range(1,n+1):
            # Decimal representation
            decimal_result = str(i)

            # Octal representation
            r_octal = []
            x_octal = i
            while x_octal != 0:
                quotient_octal = x_octal // 8
                remainder_octal = x_octal % 8
                r_octal.append(str(remainder_octal))
                x_octal = quotient_octal
            #octal_result = ''.join(reversed(r_octal)).rjust(3,' ')
            octal_result = ''.join(reversed(r_octal))

            # Hexadecimal representation
            decimal_to_hex = [j if j < 10 else hex(j)[2:].upper() for j in range(16)]
            r_hex = []
            x_hex = i
            while x_hex != 0:
                quotient_hex = x_hex // 16
                remainder_hex = x_hex % 16
                r_hex.append(decimal_to_hex[remainder_hex])
                x_hex = quotient_hex

            #hex_result = ''.join(map(str, reversed(r_hex))).rjust(4, ' ')
            hex_result = ''.join(map(str, reversed(r_hex)))

            # Binary representation
            binary = ''
            x = i
            while x > 0:
                remainder = x % 2
                binary = str(remainder) + binary
                x //= 2
            #binary_result = binary.rjust(4, ' ')
            binary_result = binary

            print(f"{decimal_result:>4}{octal_result:>5}{hex_result:>5}{binary_result:>6}")
            
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
'''

#basics
'''
price = 99
price = 100
print(price)

message = "Debugging"
print(message)

message = input()
print(message)


balance = 234.3
print(type(balance))
'''
'''
#input() always turns user input into a STRING
birth_year = int(input())
print(type(birth_year))

x = "55" # x is a string
y = int(x) # y is an integer ---- explicit conversion using int()
print(type(y))

x = 5 # integer
y = 2 # integer

z = x/y # float (implicit conversion)

#concat of strings x+y
x = input()
y = input()
print(x+y)
==============================================================================
#math operations between int and float --> float
x = 9
y = 3.0
print(x+y) #12.0
==============================================================================
#comparison operations------ ' < > == != >= <= '
print(30 < 25)
print(5 < 9)
print(50 > 100)

print(type(5 < 9))#<class 'bool'>
print(type(50 > 100))

print (5 == 5)
print (5 == 7)
print (5 != 7)
print (5 != 5)
print (5 <= 5)
print (5 >= 5)
==============================================================================
#logical operation --> BOOLEAN o/p
#AND --> both has to be TRUE 
#OR  --> atleast one has to be TRUE

print(True and False)#FALSE
print(False and True)#FALSE
print(True or False)#TRUE
print(False or True)#TRUE


for i in range(3):
    print("Hello")
===============================================================================
#Python doesn't mind whether you use 2 spaces or 4 spaces 
#(or any other number of spaces) as long as you are consistent.

#FOR loops for known no. of iterations
#WHILE loops for known condition to be met

for i in range(1,10):
    print(i)

seats = 1
while seats > 0:
  print("Sell ticket")
  seats = seats - 1
===============================================================================
'''
#if-else conditional statements-- used for selection/decision making in pgms
age = 15
if age >= 18:
 print("Regular price")
else: 
 print("Discount")

if age > 10:
 print("Discount")
print("Proceed to payment")

#elif (else if -- used for checking multiple conditions)
