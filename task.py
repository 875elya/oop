class Vehicle:
    vehiclecount = 0
    count = 0

    def __init__(self, make, model):
        Vehicle.count += 1
        self.make = make
        self.model = model


    @classmethod
    def increment(cls):
        cls.vehiclecount += 1


    @classmethod
    def getvehcount(cls):
        return cls.count

    def engine(self):
        print("Engine started!")




class Car(Vehicle):
    def __init__(self, make, model, numberofwheels):
        super().__init__(make, model)
        self.numberofwheels = 4

    def engine(self):
        print("Car engine started!")
        super().engine()

    def __repr__(self):
        return f"{self.make},{self.model}, {self.numberofwheels}"

class ElectricVehicle:
    def __init__(self,battery):
        self.battery = battery

class ElectricCar(Car, ElectricVehicle):
    pass

print(ElectricCar.__mro__)







ob = Vehicle("cls","b")
ob2 = Vehicle("aa","b")
ob.increment()
ob.increment()
print(Vehicle.vehiclecount)
print(Vehicle.getvehcount())
