class Vehicle:
    def __init__(self,name,vehicle_type):
        self.name=name
        self.vehicle_type=vehicle_type
        self.rented=False

class Car(Vehicle):
    def __init__(self,name):
       super().__init__(name,'Car')

class Bike(Vehicle):
    def __init__(self,name):
       Vehicle.__init__(self,name,'Bike')

class RentalService:
    def __init__(self):
        lamborgini = Car("lambhorghini")
        bmw=Car("bmw")
        yamaha = Bike("yamaha")
        self.vehicles=[lamborgini,bmw,yamaha]

    def rent_vehicle(self,name):
        for vehicle in self.vehicles:
            if vehicle.name == name and not vehicle.rented:
                vehicle.rented= True
                print(f"you have rented the {name} successfully")
                return
        print(f'{name} is not available right now')



rental_service=RentalService()
# for rent a car
rental_service.rent_vehicle('lambhorghini')
rental_service.rent_vehicle('bmw')
rental_service.rent_vehicle('lambhorghini')
rental_service.rent_vehicle('yamaha')