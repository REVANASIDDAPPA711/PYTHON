
"""1. Write a python program to accept a string and print alternate characters starting 
    from first character"""
# solution:
word = input()
n = len(word) 
for index in range(0, n, 2):
    print(word[index], end = " ")



"""2. Write a python program to accept a string and print only consonants in the given left to right order"""
# Solution:
word = input()
vowels = "aeiou"
for ch in word:
    if ch not in vowels:
       print(ch)
 


"""3. Write a python program to accept a string and print whether it is a palindrome or not""" 
# Solution:
word = input()
reverseWord = word[::-1]
if word == reverseWord:
  print("Palindrome")
else:
  print("Not a palindrome")



"""4. Write a python program to accept string print number of upper-case characters and number of lower-case 
  characters and number of special characters in given string"""
# Solution:
word = input()
upperCount, lowerCount, specialCount = 0, 0, 0
for ch in word: 
  if ch.isalpha():
      if ch.islower():
          lowerCount += 1 
      else:
          upperCount += 1 
  else:
      specialCount += 1 
print("no.of upper-case characters", upperCount)
print("no.of lower-case characters", lowerCount)
print("no.of special characters", specialCount)



"""5. Write a python program to accept string and print total number of "ab" substring present in given string"""
# Solution:
word = input()
result = 0 
n = len(word)
for index in range(n - 1):
    if word[index] == 'a' and word[index + 1] == 'b':
        result += 1  
print(result)
 
