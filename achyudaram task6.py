#task 6
#1
'''def even_numbers():
    for i in range(1,51):
        if i%2==0:
            print(i)
print(even_numbers())

#2
def add_two_numbers(a,b=5):
    print(a+b)
add_two_numbers(6)
add_two_numbers(6,7)

#3
def math_operation():
    a=[1,2,3,4,5]
    count=0
    for i in a:
        count+=i
        print("sum:",count)
        print("average:",count/len(a))
    for i in a:
        for b in a:
            if b>i:
                print("maximum:",i)
math_operation()

#4
def maximum(x,y,z):
    if x>y and x>z:
        return a
    else:
        if y>z:
            return y
        else:
            return z
k=maximum(3,4,5)
print(k)

#5
def student_details(name,age,height,weight):
    print("name",name)
    print("age",age)
    print("height",height)
    print("weight",weight)
student_details("achyudaram",18,188,80)

#6
def area(length,breadth):
    area=length*breadth
    print("area",area)
area(10,7)

#7
def interest(loan,interest_rate):
    interest=loan*(interest_rate/100)
    print("interest",interest)
interest(70000,5)

#8
def exponential(base,exponent=5):
    exp=base**exponent
    print("exponential":exponential)
exponential(4)

#task 9
def add(*add):
    sum=0
    for i in add:
        sum+=i
    print("sum:",sum)
add(2,67,69,5)

#task 10(incomplete)
def maxi(*maxi):
    largest=0
    for i in maxi:
        if i>largest:
            largest=i
    print("largest:",largest)
maxi(2,67,69,5)

#task 11
def display(**display):
    for i in display:
        print(i,display[i])
display(name="achu",age=23,height=188,weight=80)

#task 12
def display(**display):
    for i in display:
        print(i,display[i])
display(name="achu",age=23,height=188,weight=80)

#task 13
c=lambda a:(a**2)
print(c(int(input("enter your number:"))))

#task 14
c=lambda a,b:a if a>b else b
print(c(int(input("enter your number:")),int(input("enter your number:")))

#task 15
temp_in_c=[2,67,69,5]
temp_in_f=list(map(lambda x:x*1.8,temp_in_c))
print(temp_in_f)

#task 16
p=[2,4,6,8,7]
square=list(map(lambda x:x**2,p))
print(square)

#task 17
p=[1,2,3,4,5,6,7,8,9,10]
even=list(filter(lambda x:x%2==0,p))
print(even)

#task 18
p=[1,10,69,34,5,67]
q=list(filter(lambda x:x>100,p))
print(q)

#task 19
def power(a,b):
    if b==1:
        return a
    else:
        return a*power(a,b-1)
k=power(6,7)
print(k)

#task 20
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
k=fibonacci(6)
print(k)'''






































    













































