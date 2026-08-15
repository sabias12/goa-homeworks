name = input ("შეიყვანეთ სახელი")

age = int (input("შეიყვანე ასაკი"))

height = int (input('შეიყვანე სიმაღლე'))

if age <=18:
    print("სრულწლოვანი ხარ")
    
    
if height >= 170:
    print("მაღალი ხარ")
    
 
 
num1 = int(input("შეიყვანე პირველი რიცხვი"))
num2 = int(input("შეიყვანე მეორე რიცხი"))

if num1 and num2 >=0:
    print("რიცხვი დადებითია")
    

name = input("სეიყვანე სახელი")

balance = int (input("შეიყვანე ბალანსზე არსებული თანხა"))

vip = input("vip მპმხმარებელი ხარ? (True/False)")


if balance >= 100:
    print("ბალანსზე 100 ლარზე მეტია")
else:
    print("ბალანსზე 100 ლარზე ნაკლები გაქვს")
    
if vip =="True":
    print("vip ხარ")
else:
    print("არ ხარ")
    
