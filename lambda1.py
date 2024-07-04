#while loop
def sum_until(condition):
    total =0
    i=1
    while not condition(total):
        total +=i
        i+=1
    return total
condition=lambda x:x>=100
result=sum_until(condition)
print(result)


print("#")

#for loop
def sum_until(number,condition):
    total=0
    for num in numbers:
        if condition(total):
            break
        total+=num
    return total
numbers=[1,2,3,4,5,6,7,8,9,10]
condition=lambda x:x>=15
result=sum_until(numbers,condition)
print(result)
