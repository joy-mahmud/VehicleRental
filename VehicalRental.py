
class Vehicle:
    def __init__(self,name,vehicle_type):
        self.name=name
        self.vehicle_type=vehicle_type
        self.rented=False
userList=[]
class CreateUser:
    def __init__(self,id,username,role):
        userList.append(User(id,username,role))

class User:
    def __init__(self,id,username,role):
        self.id=id
        self.username=username
        self.role=role


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
        self.users = {"joy": "admin", "rohim": "user"}
    def add_vehicles(self,username,vehicle_name,vehicle_type):
        try:
            if(self.users[username]=='admin'):
                if (vehicle_type == "car"):
                    new_vehicle = Car(vehicle_name)
                    self.vehicles.append(new_vehicle)
                elif(vehicle_type=="bike"):
                    new_vehice = Bike(vehicle_name)
                    self.vehicles.append(new_vehice)
            elif(self.users[username]=="user"): print("Only admin can add vehicles")
        except:
            print("you are not registered yet")
    def rent_vehicle(self,name):
        for vehicle in self.vehicles:
            if vehicle.name == name and not vehicle.rented:
                vehicle.rented= True
                print(f"you have rented the {name} successfully")
                return
        print(f'{name} is not available right now')



rental_service=RentalService()
# for rent a car
# rental_service.rent_vehicle('lambhorghini')
# rental_service.rent_vehicle('bmw')
# rental_service.rent_vehicle('lambhorghini')
# rental_service.rent_vehicle('yamaha')

# rental_service.add_vehicles('joy','ferrari','car')
#
# rental_service.rent_vehicle('ferrari')
# rental_service.add_vehicles('rohim','ferrari','car')

CreateUser(101,"joy","admin")
CreateUser(102,"mahmud","user")
print(userList)