# ლოგიკური ოპერატორები გამოიყენება ორი ან მეტი პიტობის შესაფარებლად. მათი დახმარებით პროგრამა ამპოწმებს არის თუ არა პირობა true or false

name = input ("შეიყვანე შეინი სახელი")

age  = int (input("სეიყვანე შენი ასაკი"))

my_name = "saba"

if name  == my_name and age >= 18:
    print(True)
else:
    print(False)
    
gmail = input("შეიყვანე gmail:")
password = input("შეიყვანე password")
isStudent = input("შეიყვანე true ან false")

if gmail == "sabasabuka8888gmail.com" and password == "1234" and isStudent == "True":
    print(True)
else:
    print(False)