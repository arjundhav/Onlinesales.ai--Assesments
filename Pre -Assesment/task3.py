""" 
Task 2: Debugging 

 Given below is a Bash / Python script that performs following computation on an integer input (n):
    If n is less than 10: Calculate its Square
    Example: 4 => 16

    If n is between 10 and 20: Calculate the factorial of (n-10)
    Example: 15 => 120

    If n is greater than 20: Calculate the sum of all integers between 1 and (n-20)
    Example: 25 => 15

    The task is to identify the bugs in the script, fix them and share the new script. 
    Only one of the two scripts required Bash or Python. Hint: You can correct the script by only changing 3-4 characters.

"""

#Corrections
"""
  In the given python script the range for second condition is given as range(1,n-10) which is incorrect,that must be corrected as range(1,n-9).
  Similarly, for third condition the range (n-20) is incorrect which must be corrected as (n-19)
  Also, the integer division operator is used which must be corrected as floor division operator.     
"""

def compute(n):
    if n < 10:
        out = n ** 2
    elif 10 <= n < 20:
        out = 1
        for i in range(1, n - 9):        # Adjusted range from (n-9)
            out *= i
           
    else:
        lim = n - 19      # Adjusted range
        out = lim * lim
        out = out - lim
        out = out // 2  # Corrected integer division operator

    print(out)

n = int(input("Enter an integer: "))
compute(n)