digit = int(input("Enter a digit:"))
num =digit
result=0
size = len(str(digit))
while num>0:
    last_digit = num%10
    result += last_digit**size
    num = num//10

print(result)
