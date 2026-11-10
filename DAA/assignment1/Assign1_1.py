
# Write a recursive program to calculate Fibonacci numbers and find its step count.
stepCount = 0
def calculateFibonacci(termIndex):
   global stepCount
   stepCount = stepCount + 1
   if termIndex <= 1:
       return termIndex
   else:  
       return calculateFibonacci(termIndex - 1) + calculateFibonacci(termIndex - 2)
# take input from the user  


termCount = int(input("How many terms? "))
# check if the number of terms is valid  
if termCount <= 0:
   print("Please enter a positive integer")
else:  
   print("Fibonacci sequence:")  
   for termIndex in range(termCount):
       print(calculateFibonacci(termIndex))


print("Steps required using Counter ", stepCount)

         
