def fibo(n):
    if n<0:
        print("Incorrect input:")
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
num=int(input("Enter the number of terms:"))
for i in range(num):
    print(fibo(i))
        
        
