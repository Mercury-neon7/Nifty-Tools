class Airplane:
    def __init__(self, name):
        self.name = name
        self.engine = False
        self.flaps = False
        self.wheels = True
 
    def check(self):
        choice = int(input("check 1. engine 2. flaps 3. wheels: "))
        if choice == 1:
            print(f"Engine status: {self.engine}")
        elif choice == 2:
            print(f"Flaps status: {self.flaps}")
        elif choice == 3:
            print(f"Wheels status: {self.wheels}")
        else:
            print("invalid choice")
    
    def toggle(self, attribute):
        if attribute == "engine":
            self.engine = not self.engine
            print(f"Engine toggled {self.engine}")
        elif attribute == "flaps":
            self.flaps = not self.flaps
            print(f"Flaps toggled {self.flaps}")
        elif attribute == "wheels":
            self.wheels = not self.wheels
            print(f"Wheels toggled {self.wheels}")
        else:
            print("invalid statement")
 
 
class AirplaneFleet:
    def __init__(self):
        self.planes = []
    
    def add(self, name):
        new_plane = Airplane(name)
        self.planes.append(new_plane)
 
    def remove(self, name):
        for plane in self.planes:
            if plane.name == name:
                self.planes.remove(plane)
                print(f"plane {name} has been removed")
                break
        else:
            print("plane not found")
 
    def list_plane(self):
        print("Available Planes:")
        for index, plane in enumerate(self.planes):
            print(f"{index + 1}. {plane.name}")
 
    def toggle_plane(self, name, attribute):
        for plane in self.planes:
            if plane.name == name:
                if attribute == 'engine':
                    plane.toggle('engine')
                elif attribute == 'flaps':
                    plane.toggle('flaps')
                elif attribute == 'wheels':
                    plane.toggle('wheels')
                break
        else:
            print("plane not found")
    
    def check_plane(self, name):
        for plane in self.planes:
            if plane.name == name:
                plane.check()
                break
        else:
            print("plane not found")
 
#how to use:
 
# name = AirplaneFleet() - instantiates the class
# name.add("name") - adds a plane
# name.remove("name") - removes a plane
# name.list_plane() - shows the list of planes
# name.toggle_plane("name", "attribute") - toggles a plane
# name.check_plane("name") - checks the boolean attribute of a plane
