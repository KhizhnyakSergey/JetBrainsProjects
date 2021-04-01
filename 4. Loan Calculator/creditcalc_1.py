principal = int(input("Enter the loan principal: "))
print('''What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:''')
choice = input()
if choice == "m":
    print("Enter the monthly payment: ")
    money = int(input())
    print()
    payment = principal / money
    payment = round(payment)
    if payment == 1:
        print(f'it will take {payment} month to repay the loan')
    else:
        print(f'it will take {payment} months to repay the loan')
elif choice == "p":
    print("Enter the number of months: ")
    months = int(input())
    print()
    payment = principal / months
    if payment / int(payment) == 1:
        print(f'Your monthly payment = {int(payment)}')
    elif payment / int(payment) > 1:
        payment += 1
        payment = int(payment)
        lastpayment = principal - (months - 1) * payment
        print(f'Your monthly payment = {payment} and the last payment = {lastpayment}.')
