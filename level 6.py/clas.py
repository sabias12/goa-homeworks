for i in range(10):
    print("saba")
    
for i in range(0, 5, 30):
    
    print(i)
    
start = int(input("შეიყვანეთ start(საიდან): "))

stop = int (input("შეიყვანეთ stop)(რომელ რიხცვამდე): ")) 

step = int(input("შეიყვანეთ step)(ნაბიჯი):"))

for i in range(start, stop, step,):
    print(i)
    
n = int(input("შეიყვანე n )(რამდენჯერ განმეორდეს):"))

for i in range(n):
    print(f" გამეორება{i+1}")
    
number = int("შემოიყვანეთ რიცხვი")    

ჯამი = 0 
for i in range(1, number + 1):
    
    ჯამი = ჯამი + i
    
    print(f"1-დან {number}- მდე რიცხვის ჯამი: {ჯამი}")
          
