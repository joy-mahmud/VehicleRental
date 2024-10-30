import my_module
class Vehicle:
    def __init__(self, name, vehicle_type):
        self.name = name
        self.vehicle_type = vehicle_type
        self.rented = False

    def __str__(self):
        return f"{self.name}({self.vehicle_type})"


class UserControl:
    def __init__(self):
        self.userList = []

    def add_user(self, currentUser, userid, username, role):
        if currentUser.role == 'admin':
            self.userList.append(User(userid, username, role))
            print("User has been added successfully.")
        else:
            print("You are not an admin.")

    def modify_user(self, currentUser, userid, new_username=None, new_role=None):
        if currentUser.role == 'admin':
            for user in self.userList:
                if user.id == userid:
                    if new_username:
                        user.username = new_username
                    if new_role:
                        user.role = new_role
                    print(f"Data of ID:{userid} has been changed successfully.")
                    return
            print("User ID not found.")
        else:
            print("You are not an admin.")


class User:
    def __init__(self, id, username, role):
        self.id = id
        self.username = username
        self.role = role

    def __str__(self):
        return self.username


class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name, 'Car')


class Bike(Vehicle):
    def __init__(self, name):
        super().__init__(name, 'Bike')


class RentalService:
    def __init__(self):
        lamborghini = Car("Lamborghini")
        bmw = Car("BMW")
        yamaha = Bike("Yamaha")
        self.vehicles = [lamborghini, bmw, yamaha]

    def add_vehicles(self, user, vehicle_name, vehicle_type):
        try:
            if user.role == 'admin':
                if vehicle_type == "car":
                    new_vehicle = Car(vehicle_name)
                    self.vehicles.append(new_vehicle)
                    print(f"{user.username}, you have successfully added the {vehicle_type}.")
                elif vehicle_type == "bike":
                    new_vehicle = Bike(vehicle_name)
                    self.vehicles.append(new_vehicle)
                    print(f"{user.username}, you have successfully added the {vehicle_type}.")
                else:
                    print("Vehicle type not recognized. Please choose 'car' or 'bike'.")
            else:
                print("Only admin can add vehicles.")
        except AttributeError:
            print("You are not registered yet.")

    def rent_vehicle(self, name):
        for vehicle in self.vehicles:
            if vehicle.name == name and not vehicle.rented:
                vehicle.rented = True
                print(f"You have rented the {name} successfully.")
                return
        print(f"{name} is not available right now.")


def main():
    rental_service = RentalService()
    user_control = UserControl()

    # Create an admin user
    print("Create an admin account first to proceed.")
    username = input("Enter admin username: ")
    joy = User(101, username, "admin")
    print(f"Admin {joy.username} created.")

    # Add users
    user_control.add_user(joy, 101, 'rohim', 'user')
    user_control.add_user(joy, 102, 'korim', 'user')

    # Admin adds a vehicle
    rental_service.add_vehicles(joy, "Ferrari", "car")

    # Display all users
    print("All users:")
    for user in user_control.userList:
        print(f"Username: {user.username}")

    # Renting a vehicle
    rental_service.rent_vehicle('Ferrari')
    rental_service.rent_vehicle('Yamaha')


if __name__ == '__main__':
    main()
