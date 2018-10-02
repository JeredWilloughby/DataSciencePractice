# This program calculates the minimum insurance amount on  a home based off the replacement cost.
percent_insured=80
# Set the functional header and definition for mainline logic
def showInsure():
    # Set the block statements
    replacement_amount=float(input('Enter the replacement amount: '))
    replacement_cost=replacement_amount
    print('Replacement cost:$',format(replacement_cost, ',.2f'))
    print('Percent insured:',percent_insured,'%')
    x=replacement_cost*(percent_insured/100)
    print('Minimum insurance:$',format(x,',.2f'))
# Set the calling function  
showInsure()
    
