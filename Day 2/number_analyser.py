numbers=[]
for i in range(5):
    number=float(input(f"Enter 5 subject marks {i+1}:"))
    numbers.append(number)
    
print("length =",len(numbers))
print("Highest =",max(numbers))
print("lowest =",min(numbers))
print("Sum =",sum(numbers))
print("Average =",(sum(numbers)/len(numbers)))