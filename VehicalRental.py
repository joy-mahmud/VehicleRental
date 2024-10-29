
class Vehicle:
    def __init__(self,name,vehicle_type):
        self.name=name
        self.vehicle_type=vehicle_type
        self.rented=False
    def __str__(self):
        return f"{self.name}({self.vehicle_type})"
class UserControl:
    def __init__(self):
        self.userList=[]

    def add_user(self, currentUser, userid,username,role):
        if currentUser.role == 'admin':
            self.userList.append(User(userid,username,role))
            print(f"user has been added successfully")
            return
        else:
            print("you are not an admin")

    def modify_user(self, currentUser, userid, new_username: None, new_role: None):
        if currentUser.role == 'admin':
            for user in self.userList:
                if user.id == userid:
                    if new_username:
                        user.username = new_username
                    if new_role:
                        user.role = new_role
                print(f"data of id:{userid} has been changed successfully")
                return
        else:
            print("you are not an admin")

class User:
    def __init__(self,id,username,role):
        self.id=id
        self.username=username
        self.role=role

    def __str__(self):
        return self.username

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

    def add_vehicles(self,user,vehicle_name,vehicle_type):
        try:
            if(user.role=='admin'):
                if (vehicle_type == "car"):
                    new_vehicle = Car(vehicle_name)
                    self.vehicles.append(new_vehicle)
                    print(f"{user.username},you have successfully added the {vehicle_type}")
                elif(vehicle_type=="bike"):
                    new_vehice = Bike(vehicle_name)
                    self.vehicles.append(new_vehice)
                    print(f"{user.username},you have successfully added the {vehicle_type}")
            elif(user.role=="user"): print("Only admin can add vehicles")
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
user_control=UserControl()
print("Create an admin account first to proceed.")
username=input("Enter username:")
joy = User(101,username,"admin")
print(joy)
user_control.add_user(joy,101,'rohim','user')
user_control.add_user(joy,102,'korim','user')
rental_service.add_vehicles(joy,"ferrari","car")
print('all users:')
print(Vehicle('bmw','car'))
for user in user_control.userList:
    print(f'username:{user.username}')

