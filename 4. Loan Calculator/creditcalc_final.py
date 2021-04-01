import math
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--type")
parser.add_argument("--principal")
parser.add_argument("--payment")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()
full = [args.type, args.principal, args.payment, args.periods, args.interest]
float_num = []

def diff_func(P, n, i):
    m = 1
    D = (P / n) + i * (P - ((P * (m - 1)) / n))
    sum = 0

    while m < i_i + 1:
        D = (P / n) + i * (P - ((P * (m - 1)) / n))
        D = math.ceil(D)
        sum += D
        print(f'Month {m}: payment is {D}')
        m += 1
    print()
    print("Overpayment =", int(sum - P))

def annuity_1(D, n, i):
    P = D / ((i * (math.pow(1 + i, n))) / ((math.pow(1 + i, n)) - 1))
    print(f'Your loan principal = {math.floor(P)}!')
    Overpayment = (D * n) - math.floor(P)
    print("Overpayment =", math.ceil(Overpayment))

def annuity_2(D, P, i):
    n = math.ceil(math.log((D / (D - i * P)), 1 + i))
    result = int(n / 12)
    final_n = result * 12
    final_n_1 = n - final_n
    if final_n_1 == 0:
        print(f'It will take {result} years to repay this loan!')
    else:
        print(f'It will take {result} years and {final_n_1} months to repay this loan!')
    Overpayment = (D * n) - math.floor(P)
    print("Overpayment =", math.ceil(Overpayment))

def annuity_3(P, n, i):
    A = P * ((i * (math.pow(1 + i, n))) / ((math.pow(1 + i, n)) - 1))
    print(f'Your monthly payment = {math.ceil(A)}!')
    Overpayment = (math.ceil(A) * n) - math.floor(P)
    print("Overpayment =", int(Overpayment))

for num in full:
    try:
        y = float(num)
        if y > 0:
            float_num.append(num)
    except:
        pass

if args.type == None or len(float_num) < 3:
    print("Incorrect parameters.")
elif args.type == 'diff':
    if args.principal in float_num and args.periods in float_num and args.interest in float_num:
        P = float(args.principal)
        n = float(args.periods)
        i = float(args.interest)
        i_i = i
        i = i / (12 * 100)
        diff_func(P, n, i)
    else:
        print("Incorrect parameters.")
elif args.type == 'annuity' and args.payment in float_num and args.periods in float_num and args.interest in float_num:
    D = float(args.payment)
    n = float(args.periods)
    i = float(args.interest)
    i_i = i
    i = i / (12 * 100)
    annuity_1(D, n, i)
elif args.type == 'annuity' and args.principal in float_num and args.payment in float_num and args.interest in float_num:
    D = float(args.payment)
    P = float(args.principal)
    i = float(args.interest)
    i_i = i
    i = i / (12 * 100)
    annuity_2(D, P, i)
elif args.type == 'annuity' and args.principal in float_num and args.periods in float_num and args.interest in float_num:
    P = float(args.principal)
    n = float(args.periods)
    i = float(args.interest)
    i_i = i
    i = i / (12 * 100)
    annuity_3(P, n, i)
else:
    print("Incorrect parameters.")
