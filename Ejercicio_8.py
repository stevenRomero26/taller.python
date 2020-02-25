numero=int(input("digite un numero "))
for e in range(numero):
 if(e%3==0 and e%5==0):
    print(e," es","FizzBuzz")

 elif(e%5==0):
    print(e," es","Buzz")

 elif(3 %3==0):
    print(e," es", "Fizz")
 
