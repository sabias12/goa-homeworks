number = int (input("შეიყვანე რიცხვი"))

found =False

for i in range(1,100):
    if i == number:
        found = True
    
print(found)


start = int (input("შეიყვანე start:"))

stop = int(input("შეიყვანე stop:"))

step = int (input("შეუყვანე step:"))

for  i in range(start,stop,step):
    print(i)
    

name = input("შეიყვანე შენი სახელი")
lsatneym = input('შეიყვანე გვარი')

for i in range(50):
    print(name)  
    print(lsatneym)
    
n =int(input("შეიყვანე რიცხვი"))

for  i in range(n,-1,-1):
    print(i)
    
    
n= int(input("შეიყვანე რიცხვი"))
i = 0

while i <=n:
    if i % 2==0:
        print("True")
    else: 
        print("false")
    i = i+1
    
n = int (input("შეიყვანე რიცხვი"))

i = 10

while i <=n:
    print(i)
    
    i = i + 1
    
start = int (input("შეიყვანეთ start"))

stop = int (input("შეიყვანეთ stop"))

while start <=stop:
    print(start)
    start +=1
    

name = input("შეიყვაე სახელი")

while name <=50:
    print(name)
    name = name + 1
    
    
sum = 0

num = int (input("შეიყანე რიცხვი"))

while num >=0:
    sum += num
    num = int (input("შეიყანე რიცხვი"))
    
print("გილოცვა სწორი ხარ",sum)


scear = 71

guess = int(input("შეიყვანე რიცხვი"))

while guess != scear:
    print("არასწორია სცადე მოგვიანებით")
    gues =int(input("შეიყვანე რიცხვი"))
    
print("გილოცავ სწორად გამოიცანი")