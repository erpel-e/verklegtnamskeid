from models.customer import Customer
import csv

class CustomerRepo:

    CUSTOMER_FILE = "./data/customers.csv"

    def __init__(self):
        self.__customer_list = []

    def get_customer_list(self):
        """Returns a list of all customers on file"""
        if self.__customer_list == []:
            with open(self.CUSTOMER_FILE, 'r') as customer_file:
                csv_reader = csv.DictReader(customer_file)
                for line in csv_reader:
                    customer = Customer(
                        line['name'],
                        line['ssn'], 
                        line['birthday'], 
                        line['phone'],
                        line['email'],
                        line['address'], 
                        line['driver license'], 
                        line['credit card'])
                    self.__customer_list.append(customer)
        return self.__customer_list
    
    def save_new_customer(self, name, ssn, birthday, phone, 
    email, address, driver_licence, credit_card):
        with open(self.CUSTOMER_FILE, 'a', newline='') as customer_file:
            csv_writer = csv.writer(customer_file)
            csv_writer.writerow([name,ssn,birthday,phone,email,address,
            driver_licence,credit_card])
    
    def delete_customer(self, customer):
        #delete customer from csv file
        file_content = []
        with open(self.CUSTOMER_FILE, 'r') as customer_file:
            csv_reader = csv.reader(customer_file)
            for line in csv_reader:
                if line[1] != customer.get_ssn():
                    file_content.append(line)
        with open(self.CUSTOMER_FILE, 'w', newline='') as customer_file:
            csv_writer = csv.writer(customer_file)
            csv_writer.writerow(file_content[0])
            for line in file_content:
                csv_writer.writerow(line)
        
