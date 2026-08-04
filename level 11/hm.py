age = int(input("შეიყვანე ასაკი"))

if age >=18:
    print("სრულწლოვანი ხარ")
else:
    print("არასწულწლოვანი ხარ")
    
    
num1 = int(input("შეიყვანე პირველი რიცხვი"))

num2 = int (input("შეიყვანე მეორე რიცხვი"))

if num1 and num2 >=0:
    print("ორივე დადებითია ")
else:
    print("ორუვე დადებითოი არ არის")
    
    
num = input("შეიყვანე რიცხვი")

num = int (num)

print(num * num)

point = int (input("შეიყვანე ქულა"))

if point >=90 and point <=100:
    print("a")
    
if point >= 80 and point <=89:
    print("b")
    
if point >=70 and point <=79:
    print("c")
    
if point >=60 and point <=0:
    print("d")
    
for i in range(1,20):
    print(i)
    

i = 10

while i >=0:
    print(i)
    i = i - 1
    
fruis = ["vashili","yurzeni","atami","banani","msxali"]

print(fruis[0])
print(fruis[-1])
print(2)



num = [10,20,30,40,50,]

for i in num:
    print(i)
    

num1 = int(input('შეიყვანე 1 რიცხვი'))
num2 = int(input('შეიყვანე 2 რიცხვი'))
num3 = int(input('შეიყვანე 3 რიცხვი'))
num4 = int(input('შეიყვანე 4 რიცხვი'))
num5 = int(input('შეიყვანე 5 რიცხვი'))

number =[num1, num2, num3, num4,num5]

print(number)



numbers = [10,44,33,20,40,43,22,12,]

for i in range(len(numbers)):
    if i % 2==0:
        print(numbers[i])
        


n = int(input("შეიყვანე რიცხვი"))


sum = 0

for i in range(1, n+1):
    sum = sum+1
    
print(sum)


n = int (input("შეიყვანე რიცხვი"))

i = 1

while i <=n:
    if i % 2==0:
        print(i)
    i = i + 1
    


numbers =[10,15,19,22,3,30,5,55,20]

even = 0 
odd = 0


for i in numbers:
    if i % 2 ==0:
        even = even + 1
    else:
        odd = odd + 1
    
    print("ლუწების რაოდენობა,",even)
    print("კენტების რაოდენობა,",odd)
    


numbers =[10,22,3,99,43,]

larges = number[0]

for i in numbers:
    if i >larges:
        larges = i
    
print(larges)
    
    