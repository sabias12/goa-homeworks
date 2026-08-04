num1 = [3,4,44,1,22,2,1,6,5,7,3,]

for i in num1:
    print(i)
    
    if i %2==0:
        print("ლუწია")
    else:
        print("კენტია")


contries = ["georgia","ukryne","germany","ass","cina","avstralia","polonet"]

comtry = input("შეიყვანე შენი ქვეყანა")

while comtry not in contries:
    print("ქვეყანა ვერ მოიძებნა")
    comtry = input("შეიყვანე ქვეყანა")
    
print(contries.index(comtry))


numbers = [10,20,30,40,50]

print(max(numbers))
print(sum(numbers))
print(sum(numbers) / len(numbers))

num4 =[3,54,44,333,2,1,66,54,-3,-55]

positive =0
nedative = 0
zerp = 0

for i in num4:
    if i >0:
        positive +=1
    elif i <0:
        nedative +=1
    else:
        zerp +=1
        

print("დადებითია:",positive)
print("უარყოფილია:",nedative)
print("ნულია:",zerp)


numbers = [55,4,33,1,6,66,44,76,]

bigesst = numbers[0]

for i in numbers:
    if i > bigesst:
        bigesst = i
    
print(bigesst)
        
    