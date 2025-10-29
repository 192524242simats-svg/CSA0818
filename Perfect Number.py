#Perfect Number
num=int(input("Please enter any number:"))
sum=0
for i in range(1,num):
    if(num%i==0):
        print(i)
        sum=sum+i
if(sum==num):
    print(num,"is a Perfect Number")
else:
    print(num,"is not a Perfect Number")
    
