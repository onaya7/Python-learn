def newfruits(dictionary):
    for key,val in dictionary.items():
        print(f'{key} likes eating {val}')

fruits={}
while True:
        firstname=input('Enter first name:')
        secondfruit=input('Enter second fruit:')
        fruits[firstname]=secondfruit

        another=input('Would you like to enter another value? (yes/no):')
        if another == 'yes':
            continue
        else:
            break                                               

newfruits(fruits)