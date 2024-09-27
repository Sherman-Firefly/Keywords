bill_amount=2.5
amountpaid=2.5

amount_due=amountpaid - bill_amount

if amount_due <0:
    print("Insufficient Amount paid")
    amount_due = -amount_due
elif amount_due==0:
    print("Exact pay")
    pass
else:
    print(f"amount due after payment: ${amount_due:.2f}")
    