#Arthematic operator
a=10
b=3

print("Addition:", a+b)
print("Substraction:",a-b)
print("Multiplication:",a*b)
print("Division:",a/b)
print("Double Division:",a//b)
print("Modulus:",a%b)
print("exponential:",a**b)


#simple calculator
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

print("Addition:", a+b)
print("Substraction:",a-b)
print("Multiplication:",a*b)
print("Division:",a/b)
print("Double Division:",a//b)
print("Modulus:",a%b)
print("exponential:",a**b)

#students marks Calculator
name=input("Enter student name:")
m1=int(input("Enter Python marks:"))
m2=int(input("Enter Java Marks:"))
m3=int(input("Enter SQL marks:"))
total=m1+m2+m3
average=total/3

print("\n----Student Report ----")
print("Name:",name)
print("Total:",total)
print("Average:",average)

#shoping bill calculator
price1 = int(input("Enter shirt price1"))
price2 = int(input("Enter shirt price2"))

total = price1+price2
Discount= total * 10/100

total = total - Discount

print("total:",total)






















#assignment operators
x = 10
x += 5
print(x)
x -= 2
print(x)
x*=3
print(x)

#bank balance
balance = 10000

deposit = 5000
balance += deposit
print("After Deposit:",balance)

withdraw = 2000
balance -= withdraw

print("After Withdrawal:",balance)

#comparision operator
a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

#age eligibility checker
age = int(input("Enter your age:"))

print("Eligible:", age >= 18)

#pass or fail checker
marks = int(input("Enter marks:"))

print("Passed:",marks >=40)

#login validation
correct_username = "admin"
correct_password = "1234"

username = input("Enter username:")
password = input("Enter password:")

print(username == correct_username)
print(password == correct_password)

#atm eligibility checker
balance = 10000
withdraw = 5000
print(withdraw > 0 and withdraw <= balance)

 
