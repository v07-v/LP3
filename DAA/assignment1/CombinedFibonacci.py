def calculateIterativeFibonacci(termCount):
    stepCount = 0
    previousTerm = 0
    currentTerm = 1
    fibonacciTerms = []

    for _ in range(termCount):
        fibonacciTerms.append(previousTerm)
        stepCount += 1

        nextTerm = previousTerm + currentTerm
        stepCount += 1
        previousTerm = currentTerm
        stepCount += 1
        currentTerm = nextTerm
        stepCount += 1

    return fibonacciTerms, stepCount


def calculateRecursiveFibonacci(termIndex, stepCounter):
    stepCounter[0] += 1

    if termIndex <= 1:
        return termIndex

    return (
        calculateRecursiveFibonacci(termIndex - 1, stepCounter)
        + calculateRecursiveFibonacci(termIndex - 2, stepCounter)
    )


def calculateRecursiveSequence(termCount):
    stepCounter = [0]
    fibonacciTerms = []

    for termIndex in range(termCount):
        fibonacciTerms.append(
            calculateRecursiveFibonacci(termIndex, stepCounter)
        )

    return fibonacciTerms, stepCounter[0]


termCount = int(input("Enter number of terms: "))

if termCount < 0:
    print("Please enter a non-negative integer.")
else:
    iterativeTerms, iterativeSteps = calculateIterativeFibonacci(termCount)
    recursiveTerms, recursiveSteps = calculateRecursiveSequence(termCount)

    print("\nFibonacci sequence using iteration:")
    print(*iterativeTerms)
    print("Iterative step count:", iterativeSteps)

    print("\nFibonacci sequence using recursion:")
    print(*recursiveTerms)
    print("Recursive step count:", recursiveSteps)
