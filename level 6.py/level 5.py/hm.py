name = input("შეიყვანეთ თქვენი სახელი")

age = input("შეიყვანეთ ასაკი")

haid = input("შეიყვანეთ სიმაღლე")

print(name)

print(age)

print(haid)

age = 15

if age >= 18:
    print("სსრულწლოვანი ხარ")
else:
    print("არასრულწლოვანი ხარ")
    
height = int(input("შეიყვანე შენი სიმაღლე (სმ):"))

if height  > 170:
    print('მომხმარებლის სიმაღმე 170 მეტია')
else:
    print("მომხმარებლის სიმაღლე 170 ნაკლებია")
    
    
num1 = int (input("შეიყვანეთ პირველი რიცხვი "))
num2 = int (input("შეიყვანე მეორე რიცხვი"))

if num1 > 0 and num2 >0:
    print('ორივე რიცხვი დადებითია ')
else:
    print("ორივე რიცხვი დადებითო არ არის ")
    
    
    
color =  input("შეიყავანეთ საყვარეელი ფერი")

age = int  (input("შეიყვანეთ ასაკი "))

my_color = "ლურჯი"

result = color == my_color or age < 18

print(result)



name = input("შეივანეთ სახელი :")

balance = input("შეიყვანეთ ბალანსი")

vip = input("vip ხარ? (True/false)") =="True"

result = balance >100 or vip

    
    

