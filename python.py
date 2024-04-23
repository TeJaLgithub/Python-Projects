import keyword

keyword.kwlist

a=10
print(id(a))

print(bin(15)) 
print(bin(0o7777))
print(bin(0X3456))
print(oct(34))
print(oct(0xface))
print(oct(0B11))

#Data types
#==================================
#int data type
#0B
#0X
#0o

#==================================
#float data type
f = 123.456
#f1 = 0X123.456
#f2 = 0o123.456

#exponential form
e = 1.2e3
e1 = 1.2e308 
#only till e308 python
#prints 1.2e308. Starting e309
#it prints 'inf' for infinity.

print(e1)
print(type(e1))#float

#==================================
#Complex data type
#a+bj always in this form

#a = real part
#real part can be defined using 
#and int form(hex, oct, binary, decimal)

#b = imaginary part
#imaginary part only accepts decimal
#throws syntax error

#j^2 = -1

#python is good for mathematical and scientific 
#applications cuz it has complex data types

x = 5+4j

print(x)
print(type(x))

#a and b can be both integer and float
y =3.2+1.9j

print(y)
print(type(y))

#'j' imaginary part always is formed 
#using letter j and no ther letter.
#x = 2+10i 
#SyntaxError: invalid decimal literal
#print(i)

#can perform math operations
a = 10+20j
b = 20+30j

a+b
a-b
a*b

print(a.real)
print(a.imag)

#==================================
#Bool data type
# True and False

#True = 1
#False = 0
#True+True = 2
#True+False = 1

#==================================
#String(str) data type
s = "This is a string"
print(s)
