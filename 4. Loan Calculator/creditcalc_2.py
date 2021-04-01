import math

print('''What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:''')
choice = input()

if choice == "n":
    P = int(input("Enter the loan principal:"))
    A = float(input("Enter the monthly payment:"))
    i = float(input("Enter the loan interest:"))
    i = i / (12 * 100)
    n = math.ceil(math.log((A / (A - i * P)), 1 + i))
    result = int(n / 12)
    final_n = result * 12
    final_n_1 = n - final_n
    if final_n_1 == 0:
        print(f'It will take {result} years to repay this loan!')
    else:
        print(f'It will take {result} years and {final_n_1} months to repay this loan!')
elif choice == "a":
    P = int(input("Enter the loan principal:"))
    n = int(input("Enter the number of periods:"))
    i = float(input("Enter the loan interest:"))
    i = i / (12 * 100)
    A = P * ((i * (math.pow(1 + i, n))) / ((math.pow(1 + i, n)) - 1))
    print(f'Your monthly payment = {math.ceil(A)}')
elif choice == "p":
    A = float(input("Enter the annuity payment:"))
    n = int(input("Enter the number of periods:"))
    i = float(input("Enter the loan interest:"))
    i = i / (12 * 100)
    P = A / ((i * (math.pow(1 + i, n))) / ((math.pow(1 + i, n)) - 1))
    print(f'Your loan principal = {round(P)}!')
