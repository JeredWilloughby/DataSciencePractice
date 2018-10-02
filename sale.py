# This program calculates the sales price.
def main():
    print("It's your lucky day! We're having a sale!")
    print("Please enter the merchandise's original cost, then the sales amount.")
    get_amount()
    again()
def get_amount():
    original = float(input("Original price: "))
    sale = float(input("Sale percentage: "))
    convert = sale/100
    convert2 = original*convert
    new = original-convert2
    print("The new price is:$", format(new, ',.2f'))
def again():
    more = input("Would you like us to calculate the sales price on" +
                 "another item? - (y for yes): ")
    if more == 'y' or more == 'yes':
        get_amount()
        again()
    else:
        print("Have a wonderful day and thanks for shopping with us.")
main()
          
