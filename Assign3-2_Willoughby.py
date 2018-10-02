# This program calculates a properties assessed value and property tax (0.72%)
assessment_value=60

def main():
    property_value=int(input('Enter the actual value: '))
    assessed(property_value)
def assessed(property_value):
    new_value=property_value*(assessment_value/100)
    print('Assessed value:$', format(new_value,',.2f'))
    property_tax(new_value)
def property_tax(new_value):
    tax=new_value*0.0072
    print('Property tax:$',format(tax,',.2f'))
main()
