#This program show's python's read string capability
def main():
    print('The file of observation is test.txt')
    N=5
    with open(input('Enter the name of the file:'), 'r') as input_file:
        for i in range(N):
           print(input_file.readline())
main()
