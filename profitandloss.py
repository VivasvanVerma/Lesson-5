cp = int(input("Enter Cost Price: "))
sp = int(input("Enter Selling Price: "))
if cp>sp:
    loss = cp-sp
    print("You have made a loss of {0}".format(loss))
elif cp<sp:
    profit = sp-cp
    print("You have made a profit of {0}".format(profit))
else:
    print("You have not made any profit nor loss.")