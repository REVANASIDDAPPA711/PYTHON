#Pattern-1:

n = int(input())
for row in range(1, n + 1):
   for star in range(row):
       print("*", end = "")
   print()



#Pattern-2

n = int(input())
for row in range(1, n + 1):
   for col in range(1, row + 1):
       print(col, end = "")
   print()




#Pattern-3

n = int(input())
for row in range(n):
   for col in range(n):
       print("*", end = "")
   print()




#Pattern-4

n = int(input())
spaces = 0
for row in range(n):
   for space in range(spaces):
       print(" ", end = "")
   for star in range(n):
       print("*", end = "")
   spaces += 1
   print()




#Pattern-5

n = int(input())
for row in range(n, 0, -1):
   for star in range(row):
       print("*", end = "")
   print()




#Pattern-6

n = int(input())
spaces = n - 1
stars = 1
for row in range(1, n + 1):
   for space in range(spaces):
       print(" ", end = "")   
   spaces -= 1
   for star in range(stars):
       print("*", end = "")
   stars += 1
   print()




#Pattern-7

n = int(input())
spaces = n - 1
for row in range(1, n + 1):      
   for space in range(spaces):
       print(" ", end = "")
   spaces -= 1
   for col in range(1, row + 1):
       print(col, end = "")
   print()


#Pattern-8

n = int(input())
stars = n
spaces = 0
for row in range(n):
   for space in range(spaces):
       print(" ", end = "")   
   spaces += 1
   for star in range(stars):
       print("*", end = "")
   stars -= 1
   print()




#Pattern-9

n = int(input())
spaces = n - 1
stars = 1
for row in range(n):
   for space in range(spaces):
       print(" ", end = "")
   spaces -= 1
   for star in range(stars):
       print("*", end = "")
   stars += 2
   print()


#Pattern-10

n = int(input())
spaces = 0
for row in range(n, 0, -1):
   for space in range(spaces):
       print(" ", end = "")   
   spaces += 1
   for star in range(2 * row - 1):
       print("*", end = "")
   print()



#Pattern-11

n = int(input())
spaces = n - 1
for row in range(1, n + 1):      
   for space in range(spaces):
       print(" ", end = "")
   spaces -= 1
   val = 1
   for num in range(2 * row - 1):
       print(val, end = "")
       val += 1
   print()




#Pattern-12

n = int(input())
spaces = 0
for row in range(n, 0, -1):
   val = 1
   for space in range(spaces):
       print(" ", end = " ")
   spaces += 1
   for num in range(2 * row - 1):
       print(val, end = " ")
       val += 1
   print()




#Pattern-13

n = int(input())
val = 10
for i in range(1, n + 1):
   for j in range(i):
       print(val, end = " ")
       val += 10
   print()




#Pattern-14

n = int(input())
for i in range(1, n + 1):
   for j in range(i):
       if i % 2 == 0:
           print("#", end = "")
       else:
           print("*", end = "")
   print()




#Pattern-15

n = int(input())
for i in range(1, n + 1):
   val1 = i
   val2 = 1
   for j in range(i):
       if i % 2 == 0:
           print(val1, end = " ")
           val1 -= 1
       else:
           print(val2, end = " ")
           val2 += 1
   print()




#Pattern-16
	
n = int(input())
for i in range(1, n + 1):
   for j in range(i):
       if i % 2 == 0:
           print("@", end = "")
       else:
           print(i, end = "")
   print()




#Pattern-17

n = int(input())
spaces = 0
for i in range(n, 0, -1):
   for j in range(spaces):
       print(" ", end = " ")
   spaces += 1
   for j in range(2 * i - 1):
       print("*", end = " ")
   print()





#Pattern-18

n = int(input())
stars = 2 * n - 1
spaces = 0
for row in range(n):
   for space in range(spaces):
       print(" ", end = " ")
   spaces += 1
   for star in range(stars):
       print("*", end = " ")
   stars -= 2
   print()
stars += 4
spaces -= 2
for row in range(1, n):
   for space in range(spaces):
       print(" ", end = " ")
   spaces -= 1
   for star in range(stars):
       print("*", end = " ")
   stars += 2
   print()
