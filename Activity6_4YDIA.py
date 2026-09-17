#PIN Validator ------------------------9--------------------------------
pin = input('Create a 6-digit PIN: ')

try:
    if  len(pin) == 6 and pin.isdigit():
        print('Valid PIN.')
    else:
        print('Invalid PIN. Enter exactly 6 digits.')

except ValueError:
    print('Invalid PIN. Enter exactly 6 digits.')