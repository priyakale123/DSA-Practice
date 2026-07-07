def fibo(n):
    num1=0
    num2=1 
    print(num1)
    for i in range(n): 
     num3 = num1+num2
     num1, num2 = num2,num3
     print(num3)
num = int(input("enter number:"))
fibo(num)    

