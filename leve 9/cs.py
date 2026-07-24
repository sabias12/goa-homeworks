age = int (input("შეიყვანე ასაკი"))

if age >=18:
    print("you are adult")
else:
    print("you not asult")
    
    
num1 = int(input("შეიყვანე პირველი რიცხვი"))
num2 = int(input("შეიყვანე მეორე რიცხვი"))

if num1 >0 and num2 >0:
    print("ორივე რიცხვი დადებითია")
else:
    if num1 > 0 or num2 >0:
        print("მხოლოდ ერთი რიცხვია დადებითი")
    else:
        print("არცერთი რიცხვი არ არის დადებიათი")
    
    
    
    
count = 1

while count <=10:
    number = int(input("შეიყვანე  რიცხვი"))
    
    
    if number >0:
     if number % 2 == 0:
        print("რიცხვი დადებითია და ლუწია")
    else:
        print("რიცხვი დადებითია და ლუწია")
else:
    print("რიცხვი არ არის დადებითი")
    
count = count +1