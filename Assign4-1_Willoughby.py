# This program will compute a store's sales amount for each day of the week.
def main():
    # Create a list vector
    sales = []
    # Set the accumulator
    total = 0
    # Get sales amounts for each day of the week.
    S = float(input('Enter the sales for Sunday: '))
    print()
    M = float(input('Enter the sales for Monday: '))
    print()
    T = float(input('Enter the sales for Tuesday: '))
    print()
    W = float(input('Enter the sales for Wednesday: '))
    print()
    Th = float(input('Enter the sales for Thursday: '))
    print()
    F = float(input('Enter the sales for Friday: '))
    print()
    Sa = float(input('Enter the sales for Saturday: '))
    print()
    sales.append(S)
    sales.append(M)
    sales.append(T)
    sales.append(W)
    sales.append(Th)
    sales.append(F)
    sales.append(Sa)
    for value in sales:
        total += value
    print('Total sales for the week: $', format(total, ',.2f'))

main()
