point = int(input("შეიყვანე შენი ქულა"))

if point >=100:
    print("არასწორი ქულა")
elif point >90 and point <100:
    print("საუკეთესო შედეგია")
elif point >70 and point <90:
    print("კარგი შედეგია")
elif point >50 and point <70:
    print("კამაკმაყოფილებელო შედეგია")
else:
    print("ვერ ჩააბარე")
    
    
    
    
    
list = ["saba","nika","goa","dog","cat","demetre","deniel","python","js","node js"]

print(list[-4:])


name = input("შეიყვანე სახელი")


print(name[::-1])