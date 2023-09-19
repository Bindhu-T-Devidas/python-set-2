numbers=[2,2,2,34,4,4,5,6,7]
unique=[]
for n in numbers:
    if n not in unique:
        unique.append(n) 
print(unique)
