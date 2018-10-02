# This program uses three different dictionaries. It allows the user to enter a
# a course number, then display the associated room number, intructor, and time.
print("The course numbers are: ISQS 5347, ISQS 6337, ISQS 6349, ISQS 6348")
room_number = {'ISQS 5347':'BA 289', 'ISQS 6337':'BA 015', 'ISQS 6349':'BA 287',
               'ISQS 6348':'BA 021'}
name = {'ISQS 5347':'Zadeh', 'ISQS 6337':'Song', 'ISQS 6349':'Kim',
               'ISQS 6348':'Benjamin'}
time = {'ISQS 5347':'9:00 a.m.', 'ISQS 6337':'2:00 p.m.', 'ISQS 6349':'9:00 a.m.',
               'ISQS 6348':'2:00 p.m.'}

enter = input('Enter a course number to locate the details: ')
if enter in room_number and name and time:
    print('The details for course', enter, 'are:')
    print('Room:', room_number.get(enter))
    print('Instructor:', name.get(enter))
    print('Time:', time.get(enter))
    
