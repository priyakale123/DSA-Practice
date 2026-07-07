def fibo(num):
    if num==0 or num==1:
        return num
    else:
        return fibo(num-1)+fibo(num-2)
num = int(input("enter number:"))
for i in range(num):
  print(fibo(i),end=" ")  


   
