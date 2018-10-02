# This program demonstrates the class and instance capabilities of python.
#Please download the employee file that holds the class.
import Employee
def main():
    worker_name= " "
    worker_id = " "
    worker_shift = 0
    worker_pay = 0.0
    worker_name = input("Enter the worker name: ")
    worker_id = input("Enter the ID number: ")
    worker_shift = int(input("Enter the shift number: "))
    worker_pay = float(input("Enter the hourly pay rate: "))
    worker = Employee.Worker(worker_name, worker_id, worker_shift, worker_pay)
    print ("Production worker information: ")
    print ("Name: ", worker.name)
    print ("ID number: ", worker.id_number)
    print ("Shift: ", worker.shift_number)     
    print ("Hourly Pay Rate: $", format(worker.pay_rate,',.2f'))
main()
