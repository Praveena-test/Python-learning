#Factorial n = 5 5! -->54321 -> 120 3! -> 321 -> 6 4! -> 432*1 -> 24

fact_num=int(input("Enter the number to find the factorial: "))
# check if the number is negative, positive or zero
if fact_num < 0:
    print("Factorial is not applicable for negative numbers")
elif fact_num == 0:
    print("Factorial of 0 is 1")
else:
    factorial = 1
    for fact_num in range(1, fact_num+1):
        # print(fact_num)
        factorial = factorial * fact_num
    print(f"factorial of {fact_num} is: {factorial}")