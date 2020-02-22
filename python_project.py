#Prime Number Function Start
def prime():
    z = int(input("Enter number of prime numbers you want: "))
    list1 = []
    x = 1
    print("Enter numbers: ")
    while(x <= z):
        a = int(input())
        b = 0
        for i in range(2, a):
            if(a%i == 0):
                b = b + 1
                x = x - 1
        if(b == 0):
            if(a == 1):
                pass
            else:
                list1.append(a)
        x = x + 1
    print("Prime numbers are: ", list1)
#Prime Number Function End

#Factorial Function Start
def fact():
    z = int(input("Enter the number whose factorial you want: "))
    b = 1
    for i in range(1,z+1):
        b = b*i
    print("Factorial is: ", b)
#Factorial Function End

#Pallindrome Function Start
def pall():
    a = int(input("Enter the number you wanna check: "))
    b = 0
    d = a
    while(a > 0):
        c = a % 10
        b = b*10 + c
        a = a//10
    if(b == d):
        print("The given number is a pallindrome")
    else:
        print("The given number is not a pallindrome")
#Pallindrome Function End

#Fibonacci Series Function Start
def fibo():
    a = int(input("Enter the number till where you want the fibonacci series: "))
    f = 0
    l = 1
    c = 0
    i = 1
    print("The fibonacci series is: ")
    while(i <= a):
        if(i <= 1):
            c = i
        else:
            c = f + l
            f = l
            l = c
        print(c)
        i = i + 1
#Fibonacci Series Function End

#Menu Function Start
def menu():
    c = 'y'
    while(c == 'y'):
        print("1. Prime Numbers")
        print("2. Factorial")
        print("3. Pallindrome")
        print("4. Fibonacci Series")
        cho = int(input("Enter your choice: "))
        if(cho == 1):
            prime()
        elif(cho == 2):
            fact()
        elif(cho == 3):
            pall()
        elif(cho == 4):
            fibo()
        else:
            print("Wrong Input")
        c = input("Do you want to continue: ")
#Menu Function End

#Main

menu()
