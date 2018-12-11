from datetime import date


class Vehicle:
    def __init__(self, license_plate, make, model, year, type_of_vehicle, seats, fuel, transmission, maintainance=0, dates=[]):
        self.__license = license_plate
        self.__make = make
        self.__model = model
        self.__year = year
        self.__type_of_vehicle = type_of_vehicle
        self.__seats = seats
        self.__fuel = fuel
        self.__transmission = transmission
        self.__maintainance = maintainance
        self.__rent_dates = dates
        self.__rented_dates = []
        self.set_rented_dates()
        self.set_price()
        self.set_insurance()

    def set_price(self):
        if self.__type_of_vehicle == "smallcar":
            self.__price_per_day = 9000
        elif self.__type_of_vehicle == "sedan":
            self.__price_per_day = 10000
        elif self.__type_of_vehicle == "offroad":
            self.__price_per_day = 12000
        elif self.__type_of_vehicle == "bus":
            self.__price_per_day = 13000

    def set_insurance(self):
        if self.__type_of_vehicle == "smallcar":
            self.__insurance_per_day = 1050
        elif self.__type_of_vehicle == "sedan":
            self.__insurance_per_day = 1150
        elif self.__type_of_vehicle == "offroad":
            self.__insurance_per_day = 1350
        elif self.__type_of_vehicle == "bus":
            self.__insurance_per_day = 1500

    def set_rented_dates(self):
        try:
            for d in self.__rent_dates:
                rent_day = date(int(d[:4]), int(d[4:6]), int(d[6:]))
                self.__rented_dates.append(rent_day)
        except ValueError:
            pass
            
    def get_rented_dates(self):
        return self.__rented_dates

    def __str__(self):
        return "{} | {}".format(self.__license, self.__make)

    def availability_string(self):
        return '{:<20} {:<20} {:<20} {:<20}'.format(self.__license, self.__make, self.__model, self.__seats)

    def get_license(self):
        return self.__license

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_vehicle_type(self):
        return self.__type_of_vehicle

    def get_seats(self):
        return self.__seats

    def get_price_per_day(self):
        return self.__price_per_day

    def get_insurance_per_day(self):
        return self.__insurance_per_day

    def get_attributes(self):
        return (self.__license, self.__make, self.__model, self.__year, self.__type_of_vehicle, 
        self.__seats, self.__fuel, self.__transmission, self.__maintainance)
    
    def return_details(self):
        """Returns the details needed for editing the car"""
        return {
            "Car type": self.__type_of_vehicle,
            "Make": self.__make,
            "Model": self.__model,
            "Year": self.__year,
            "Number of seats": self.__seats,
            "License": self.__license,
            "Fuel": self.__fuel,
            "Driving transmission": self.__transmission,
        }
    


