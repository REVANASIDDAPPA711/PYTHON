def TotalEvenNumbers(l):
    result = 0
    n = len(l)
    for index in range(n):
        if l[index] %2 == 0:
            result= result + 1
    return result
l = [11,12,13,14,15,16,17,18,19,20]
result = TotalEvenNumbers(l)
print("total number of even numbers",result)
