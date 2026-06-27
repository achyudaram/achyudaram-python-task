#task 3
'''1
a=int(input("enter a number"))
b=a&1
if b==1:
    print("the number is odd")
elif b!=1:
    print("the number is even")

#2
a=int(input("enter a number"))
if a>0:
    print("the number is positive")
elif a<0:
    print("the number is negative")
else:
    print("zero")

#3
a=int(input("enter a number"))
b=a%10
if b==0:
    print("the given number is divisible by 2 and 5")
else:
    print("the given is not divisible by 2 and 5 at the same time")

#4
marks=int(input("enter the maks"))
if marks>=93:
    print("GradeA")
elif marks>=75:
    print("Grade B")
elif marks>=65:
    print("Grade C")
elif marks>=35:
    print("Grade D")
else:
    print("Grade E")

#5
y=int(input("enter a yeasr"))
a=y%4
b=y%100
c=y%400
if a==0:
    print("Leap year")
elif b==0:
        print("Is Not a Leap year")
elif c==0:
   print("Leap year")
else:
    print("Is Not a Leap Year")

#6
for i in range(1,11,1):
    print(i)

#7
for i in range(1,11,1):
    a=i**2
    print(a)'''

'''#8
for i in range(10,0,-1):
    print(i)

#9
y=int(input("enter your age"))
if y in range(0,13):
    print("you are a child")
elif y in range(13,20):
    print("you are a teen")
elif y in range(20,60):
    print("you are an adult")
elif y in range(60,1000):
    print("you are a senior citizen")

#10
a=int(input("enter a number"))
if a**3<=100:
    print("the cube of the number is less than or equal to 100")
else:
    print("the cube of the number is more than or equal to 100")

#11
a=input("enter the useranme")
if a=="achyudaram" :
    b=input("enter the password")
if b=="achu6967":
    print("login succesful")
elif a!="achyudaram":
    print("login unsuccesful,enter corect username")
elif b!="achu6967":
    print("login falied,enter correct password")
    
#12
a=str(input("enter an alphabet:"))
if a in ["a","e","i","o","u"]:
    print("the alphabet is a vowel")
else:
    print("the alphabet is a consonant")

#13
n=int(input("enter a natural numbera"))
print(n*(n+1)/2)

#14
p=65
for i in range(1,27):
    print(chr(p))
    p+=1
    print()

#15
a=int(input("enter a number"))
for i in range(1,11):
    print(a,"X",i,"=",a*i)
    print()
    
#16
n=int(input("enter a number"))
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()

n=int(input("enter a number"))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()

n=int(input("enter a number"))
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()

#17
n=int(input("enter a number"))
for i in range(n):
    for j in range(n):
        print(i,end=" ")
    print()
    
n=int(input("enter a number"))
for i in range(n):
    for j in range(n):
        print(j,end=" ")
    print()

n=int(input("enter a number"))
for i in range(n):
    for j in range(i+1):
        print(i,end=" ")
    print()

n=int(input("enter a number"))
for i in range(n):
    for j in range(i+1):
        print(j,end=" ")
    print()
    
n=int(input("enter a number"))
for i in range(n):
    for j in range(i,n):
        print(i,end=" ")
    print()

n=int(input("enter a number"))
for i in range(n):
    for j in range(i,n):
        print(j,end=" ")
    print()

#18
n=int(input("enter a number"))
p=65
for i in range(n):
    for j in range(i+1):
        print(chr(p),end=" ")
        p+=1
    print()

n=int(input("enter a number"))
p=65
for i in range(n):
    for j in range(i,n):
        print(chr(p),end=" ")
        p+=1
    print()

#19
correct_password=67676969
while 'true':
    password=int(input("enter your password:"))
    if password==correct_password:
        print("access granted")
        break
    else:
        print("incorrect password","try again")'''














































 



















    


    

    

