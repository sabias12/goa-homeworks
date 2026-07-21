n = int (input("შეიყვანე რიცხვი"))

for i in range(1, n + 1):
    print(i)
    
    
start = int (input("შეიყვანე start:"))

stop = int (input("შეიყვანეstop:"))

step = int (input("შეიყვანე step"))

for i in range (start, stop, step,):
    print(i)
    
    
start = int(input("შეიყვანეთ საწყისი რიცხვი"))

stop = int(input("შეიყვაეთ საბოლოო რიცხვი"))

for i in range(start, stop + 1):
    if i <50:
        print(i)
        
        
n = int(input("შეიყვანე რიცხვი"))
    
for i in range(n, -1,-1,):
    print(i)
    

    
n = int (input("შეიყვანე რიცხვი:"))

i = 0

while i <=n:
    print(True)
else:
    print(False)
    
i = i + 1



n = int (input("შეოყვანეთ რიცვი"))

for i in range(10,n+1,):
    print(i)
    
    
start = int(input("შეიყვანე start"))
stop = int (input('შეიყვანე stop'))

while start<= stop:
    print(start)
    start = start +1
    


name = input('შეიყვანე სახელი')

i = 0

while i<50:
    print(name)
    i = i + 1
    


sum = 0

number = int (input('შეიყვანე რიცხვი'))

while number >=0:
    sum = sum +number
    
    number = int (input("შეიყვანე რიცხვი"))
    
print(sum)


sceret = 73

guess = int (input("გამოიცანი რიცხვი"))

while guess!=sceret:
    guess = int (input("არასწორი სწადე ხელახლა "))
    
print("გილოცცავ სწორი ხარ")