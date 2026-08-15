

def filter_evens(numbers):
    evens=[]
    
    for i in numbers:
        if i % 2 == 0:
            evens.append(i)
        
        return evens 
    
    
def sum_numbers(numbers):
    total = 0
    
    for i in numbers:
        total +=1
        
    return total
        
numbers =[1,2,3,4,5,6,7,8,9,10]
    
    
result = filter_evens(numbers)
print(sum_numbers(result))
    



def positives (num):
    positives_array = []
    
    for i in num:
        if i >0:
            positives_array.append(i)
            
        return positives_array
    
    
    
def filter_odds(numbers):
    odds =[]
    
    for i in numbers:
        if i % 2==1:
            odds.append(i)
            
    return odds


def sum_numbers(numbers):
    total = 0
    
    for i in numbers:
        total +=1
        
    return total

numbers = [-3,-43,-44,-4,-76,-32,-4,10]

positive_result = positives(numbers)
odd_result = filter_odds(positive_result)

print(positive_result)
print(odd_result)
print(sum_numbers(odd_result))
