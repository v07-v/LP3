
# Write an iterative program to calculate Fibonacci numbers and find its step count.
stepCount = 0
termCount = int(input("Enter Number of Terms :"))
previousTerm = 0
currentTerm = 1
printedTerms = 0
if(termCount < 0):
    print("Enter valid input..")
elif(termCount == 0):
    print(0)
elif(termCount == 1):
    print("Fibonacci series upto", termCount, "is", previousTerm)
else:
    while printedTerms < termCount:
        print(previousTerm)
        stepCount = stepCount + 1
        nextTerm = previousTerm + currentTerm
        stepCount = stepCount + 1
        previousTerm = currentTerm
        stepCount = stepCount + 1
        currentTerm = nextTerm
        stepCount = stepCount + 1
        printedTerms += 1
        stepCount = stepCount + 1
        

print("Steps required using Counter ", stepCount)
     
