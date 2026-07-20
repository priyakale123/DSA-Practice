num = int(input("Enter number:"))
temp = num
exp = len(str(num))
sum=0
while temp>0:
   
        rev = temp %10
        sum = sum+ rev**exp   
        temp=temp//10
        
if sum==num:
        print("number is armstrong",sum) 
else:
        print("not armstrong")               
