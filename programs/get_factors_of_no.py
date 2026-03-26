num = int(input("Enter a number:"))
result = []
for i in range(1,num//2):
    if num % i==0:
        result.append(i)
result.append(num)
print(result)