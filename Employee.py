class Employee(object):
    def __init__(self, name, id_number):
        self.id_number = id_number
        self.name = name
class Worker(Employee):
    def __init__(self, name, id_number, shift_number, pay_rate):
        Employee.__init__(self, name, id_number)
        self.shift_number = shift_number
        self.pay_rate = pay_rate
