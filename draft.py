from time import perf_counter


# 2.1
def func(initialBalance, interestRate, paymentRate, termLength):
    unpaid = initialBalance
    monthlyInt = interestRate/12
    for i in range(termLength):
        paidBalance = unpaid - (unpaid*paymentRate)
        unpaid = paidBalance + (paidBalance * monthlyInt)
    print("remaining balance: %.2f" % unpaid)


func(5000, .18, .02, 12)


# 2.2
def func2(initialBalance, interestRate, termLength):
    balance = initialBalance
    payment = 0
    monthlyInt = interestRate/12
    while (balance > 0):
        balance = initialBalance
        payment += 10
        for i in range(termLength):
            paidBalance = balance - payment
            balance = paidBalance + (paidBalance * monthlyInt)
    print('Lowest payment: ' + str(payment))


amount = input('enter a starting balance: ')
start = perf_counter()
func2(int(amount), .18, 12)
end = perf_counter()
print(end - start)


# 2.4
