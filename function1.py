def area(r):
    A=3.14*r**2
    return A
def square(a):
    x=a**2
    return x
def convertcel():
   f=(c*9/5)+32
   print("The value in Fahrenheit",f)
def convertfah():
    c=(f-32)*5/9
    print("The Value in celsius",c)
def maximum():
    first=int(input("Enter the 1st number:"))
    second=int(input("Enter the 2nd number:"))
    print("The highest value is",max(first,second))   
b=int(input("Enter a value for squaring:"))
print(square(b))
a=int(input("Enter the value of radius:"))
print(area(a))
c=float(input("Enter the Value of celsius:"))
convertcel()
f=float(input("Enter the Values of fahrenheit:"))
convertfah()
maximum()
