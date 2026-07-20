i = 0

while i <= 0:
    print(i)
    i = i + 1
    
i = 10




while i <= 10:
    print(i)
    i = i - 1
    
i = 0
sum = 0



while i <= 5:
    sum = sum + i
    i = i + 1
    
print(sum)



name = input("შეიყვანე სახელი")

n=  int(input("შეიყვანე რიცხვი"))

i = 0 

while i <n:
    print(name)
    i = i +1
    
    
    
password = "pythone123"

user_password = input("შეიყვანე პაროლი:")

while user_password != password:
    user_password = input("არასწორი პაროლი სცადეთ თავიდან:")
    
print("access granted")
