#This program shows class programming. Please download the cellphone class file
#before running this file.
import cellphone
def main():
    manufact = input('Enter the manufacturer:')
    model = input('Enter the model number:')
    price = float(input('Enter the retail price:'))
    phone = cellphone.cellphone(manufact, model, price)
    print('Here is the data that you entered:')
    print('Manufacturer:', phone.get_manufact())
    print('Model Number:', phone.get_model())
    print('Retail Price:$', format(phone.get_retail_price(), ',.2f'), sep='')
main()
