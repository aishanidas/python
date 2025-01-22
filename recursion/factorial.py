num = int(input("Enter an integer to calculate factorial: "))

def factorial(num):
    if num ==1:
        return num
    else:
        return num*factorial(num-1)


print("Calculated factorial: " + str(factorial(num)))