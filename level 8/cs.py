i = 0

while i <=10:
    print(i)
    i = i + 1
    
i = 10

while i >=0:
    print(i)
    i = i - 1
    
i = 0

total = 0

while i <= 5:
    total = total + i
    
    i += 1
    
print(total)



n = int(input("შეიყვანეთ რიხ=ცხვი:"))

i = 0

while i <=n:
    print(i)
    i += 1
    

password = input("შეიყვანეთ პაროლი")

while password != "python123":
    password = input("არასწორია სცადეთ მოგვიანებით")

print("acces granted")