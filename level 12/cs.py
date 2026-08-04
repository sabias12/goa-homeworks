name = input("შეიყვანე ასაკი")

if name >=0:
    print("შქვენი ასალკი დადებითია")
else:
    print("ასაკი დადებითი არ არის")


weak = ["ორშაბათი","სამშაბათი","ოთხშაბათი","ხუთშაბათი","პარასკევი","შაბათი","კვირა"]

index = int (input("შეიყვანე index"))

print(weak[index])

list = [33,"python","goa","True","Fools","student",6.3,77,"mentor","academi","tbilisi","georgia"]

cost = 0

for i in list:
    cost +=1
    
print(cost)

list = [4,44,3,22,1,55,43,66,7,44,345,54,]

for i in range(len(list)):
    if i %2==0:
        print(list[i])