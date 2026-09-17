# 1 --------PAYMENT METHOD CHECKER----------------


methods = ['cash', 'gcash', 'card']
method = input("Enter payment method: ")
if method.lower() in methods:
    print('Valid payment method.')
else:
    print('Invalid method.')