str=input("Enter a string:")
v_count=0
c_count=0
vowels="aeiouAEIOU"
v=[]
c=[]
for i in range(0,len(str)):
    if str[i]in (vowels):
        v_count+=1
        v.append(str[i])
    elif(str[i]!=" " and str[i] not in(vowels)):
        c_count+=1
        c.append(str[i])
print("Total number of vowels & consonants are:")
print(v_count,v)
print(c_count,c)
