#Bubble Sort

n = int(input())
l = list(map(int, input().split()))
fixThis = n - 1
while fixThis > 0:
   for index in range(fixThis):
       if l[index] > l[index + 1]:
           l[index], l[index + 1] = l[index + 1], l[index]
   fixThis -= 1
print(*l)


#Selection Sort

n = int(input())
l = list(map(int, input().split()))
fixThis = n - 1
while fixThis > 0:
   maxIndex = fixThis
   for index in range(fixThis):
       if l[index] > l[maxIndex]:
           maxIndex = index
   if maxIndex != fixThis:
       l[maxIndex], l[fixThis] = l[fixThis], l[maxIndex]
   fixThis -= 1
print(*l)


#Insertion Sort

n = int(input())
l = list(map(int, input().split()))
for index in range(1, n):
   position = index - 1
   temp = l[index]
   while position >= 0:
       if l[position] > temp:
           l[position + 1] = l[position]
       else:
           break
       position -= 1
   l[position + 1] = temp          
print(*l)


#Merge Sort

def mergeThese(l, left, mid, right):
   temp = []
   index1 = left
   index2 = mid + 1
   while index1 <= mid and index2 <= right:
       if l[index1] > l[index2]:
           temp.append(l[index2])
           index2 += 1
       else:
           temp.append(l[index1])
           index1 += 1       
   while index1 <= mid:
       temp.append(l[index1])
       index1 += 1  
   while index2 <= right:
       temp.append(l[index2])
       index2 += 1   
   position = 0
   for index in range(left, right + 1):
       l[index] = temp[position]
       position += 1
def divideIt(l, left, right):
   if left == right:
       return
   mid = (left + right) // 2
   divideIt(l, left, mid)
   divideIt(l, mid + 1, right)
   mergeThese(l, left, mid, right)
def mergeSort(l):
   divideIt(l, 0, len(l) - 1)
n = int(input())
l = list(map(int, input().split()))
mergeSort(l)          
print(*l)


#Quick Sort

def findPosition(l, left, right):
   pivot = l[right]
   position = left
   index = left
   while index < right:
       if l[index] < pivot:
           l[position], l[index] = l[index], l[position]
           position += 1
       index += 1   
   l[position], l[right] = l[right], l[position]
   return position  
def divideIt(l, left, right):
   if left >= right:
       return
   position = findPosition(l, left, right)
   divideIt(l, left, position - 1)
   divideIt(l, position + 1, right)
def quickSort(l):
   divideIt(l, 0, len(l) - 1)
n = int(input())
l = list(map(int, input().split()))
quickSort(l)      
print(*l)
