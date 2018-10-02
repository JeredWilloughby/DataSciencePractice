# This program demonstrates python's File input and Output capability.
def main():
    outfile = open('numbers.txt', 'w')

    outfile.write('22\n')

    outfile.write('-99\n')

    outfile.write('55\n')
    outfile.close()
    read()
def read():
    infile = open('numbers.txt', 'r')
    file_contents = infile.read()
    infile.close()
    print(file_contents)
main()
