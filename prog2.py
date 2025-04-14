actual_cost = float(input("please Enter the actual product price: "))
sale_amount = float(input("please Enter the actual product price: "))

if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("Total Profit = {}".format(amount))
else:
    print("No Profit!!!")
    