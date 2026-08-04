age = int (input("შეიყვაბე ასაკი"))
status = input("შეიყვანე მოქალაქეობის სტატუსი")

if age >=18 and status =="moqalaqe":
    print("შესვალე ნებადართულია")
else:
    print("შესვლა აკრძალულია")
    
    
numbers = [10,33,2,44,3,5,33,1,]

for i in numbers:
    if i >10:
        print(i)



citi = ["tbilisi","batumi","coxatauri","new york","ozurgeti","mcxeta"]

index = int (input("შეიყვანნე ინდექსი"))

print(citi[index])


num1 = int(input("შეიყვანე  რიცხვი1"))
num2 = int(input("შშეიყვანე რიცხვი2"))

if num1 >100 or num2 >100:
    print("პირობა შესრულდა")
else:
    print("პირობა ვერ შესრულდა")


num1 = [1,22,32,2,3,11,99,4,33,22,44]


for num in num1:
    if num % 2 ==0:
        print(num)



xili = ["ვაშლი","ბანანი","საზამთრო","ნესვი","ატამი","ვაშლ ატამა","მსხალი","მარწყვი","ყურძენი"]

new_list = xili [:5]

print(new_list)


num3 = [33,333,22,1111,65,555,333,3,44]
i =0

while i <len(num3):
    if num3[i]>100:
        print(num3[i])
        
    i +=1




num4 = [3,22,33,3,2,11,22,3,22,0]

neww_num = num4[::2]

print(neww_num)



num5 = [44,444,3,222,50,54,33,22,3,333]

for i in num5:
    if i >50 or i <0:
        print("დიდია")
    else:
        print('ნორმალურია')
        
        


temp = int(input("შეიყვანე ტემპერატურა"))

if temp <0 or temp >35:
     print("ექსტრემალური ტემპერატურა")
else:
     print("ნორმალური ტემპერატურა")
    


