amount_due=50
while amount_due>0:
    coin=int(input('Insert Coin: '))
    if coin in [5,10,25,50]:
        amount_due=amount_due-coin
        if amount_due>0:
            print('Amount Due:',amount_due)
    else:
        if amount_due>0:
            print('Amount Due:',amount_due)
print('Change Owed:',amount_due*(-1))
