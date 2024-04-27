def findGreatestElement(numbers):
    result= 0
    n= len(numbers)
    for index in range(n):
        if numbers[index] > result:
            result = numbers[index]
    return result    
numbers = [8,7,32,45,22,47,52,444,143,989,4321,421,543,678,2219]
result = findGreatestElement(numbers)
print("greatest element is",result)
