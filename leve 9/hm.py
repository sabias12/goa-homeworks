point = int (input("შიყვანეთ გამოცდის ქულა"))

if point >=91 and point <=100:
    print("a")
    
if point >=81 and point <=90:
    print("b")
    
if point >=71 and point <=80:
    print("c")
    
if point >=60 and point <=0:
    print("d")
    
else:
    print("f")
    
    
sum = 0

number = int(input(("შეიყვანე პირველი რიცხვი")))

max_number = number
min_number = number
sum = sum + number

for i in range(9):
    number = int (input("შეიყვანე რიცხვი"))
    sum = sum + number
    
    if number> max_number:
        max_number = number
        
    if number < min_number:
        min_number = number
            
avarage = sum / 10

print("ჯამი", sum)
print("sაშუალო",avarage)
print("უდიდესი",max_number)
print("უმცირესი",min_number)



num1 = int (input("პირველი რიცხვი"))
num2= int (input("მეორე რიცხვი"))

if num1 >= num2:
    print("პირველი რიცხვი მეტია")
elif num2 > num1:
    print("მეორე რიცხვი მეტია")
else:
    print("რიცხვები ტოლია")
    
    
password="1234"

tries = 0

while tries <3:
    user_password = input ("შეიყვანე პაროლი:")
    
    if user_password == password:
        print("წვდობა დაშვებულია")
        tries = 3
    else:
        print("არასწორი პაროლი")
        tries = tries + 1
        
if tries == 3 and user_password != password:
    print("წვდომა აკრძალულია")
    
        
    

            
    
    