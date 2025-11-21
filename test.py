from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
    
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
    @abstractmethod
    def travel(self, distance: int):
        pass
    
    def __str__(self):
        return f'{self.brand} {self.model} {self.year}. Mileage: {self.mileage} km.'

class Car(Vehicle):
    def __init__(self, brand: str, model: str, year: int):
        super().__init__(brand, model, year)
        self.engine_running = False
    
    def start(self):
        if not self.engine_running:
            self.engine_running = True
            print(f'Engine of {self.brand} {self.model} started.')
        else:
            print(f'Engine of {self.brand} {self.model} is already running.')
    
    def stop(self):
        if self.engine_running:
            self.engine_running = False
            print(f'Engine of {self.brand} {self.model} stopped.')
        else:
            print(f'Engine of {self.brand} {self.model} is already stopped.')
    
    def travel(self, distance: int):
        if self.engine_running:
            self.mileage += distance
            print(f'Car {self.brand} {self.model} traveled {distance} km. Total mileage: {self.mileage} km.')
        else:
            print(f'Start the engine of {self.brand} {self.model} first!')

class Motorcycle(Vehicle):
    def __init__(self, brand: str, model: str, year: int):
        super().__init__(brand, model, year)
        self.engine_running = False
    
    def start(self):
        if not self.engine_running:
            self.engine_running = True
            print(f'Engine of {self.brand} {self.model} started.')
        else:
            print(f'Engine of {self.brand} {self.model} is already running.')
    
    def stop(self):
        if self.engine_running:
            self.engine_running = False
            print(f'Engine of {self.brand} {self.model} stopped.')
        else:
            print(f'Engine of {self.brand} {self.model} is already stopped.')
    
    def travel(self, distance: int):
        if self.engine_running:
            self.mileage += distance
            print(f'Motorcycle {self.brand} {self.model} traveled {distance} km. Total mileage: {self.mileage} km.')
        else:
            print(f'Start the engine of {self.brand} {self.model} first!')

class Bicycle(Vehicle):
    def __init__(self, type: str, brand: str, year: int):
        super().__init__(brand, "", year)
        self.type = type
    
    def start(self):
        print('Bicycle has no engine!')
    
    def stop(self):
        print('Bicycle has no engine!')
    
    def travel(self, distance: int):
        self.mileage += distance
        print(f'{self.type} bicycle "{self.brand}" traveled {distance} km. Total mileage: {self.mileage} km.')
    
    def __str__(self):
        return f'{self.type} bicycle "{self.brand}" {self.year}. Mileage: {self.mileage} km.'

class TransportPark:
    def __init__(self):
        self.vehicles = []
    
    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles.append(vehicle)
    
    def show_all_vehicles(self):
        print("=== Information about all vehicles ===")
        for vehicle in self.vehicles:
            print(vehicle)
        print()
    
    def test_drive(self):
        print("=== Starting and test driving ===")
        for vehicle in self.vehicles:
            if isinstance(vehicle, Bicycle):
                vehicle.start()
                vehicle.travel(25)
                vehicle.stop()
            elif isinstance(vehicle, Car):
                vehicle.start()
                vehicle.travel(150)
                vehicle.stop()
            elif isinstance(vehicle, Motorcycle):
                vehicle.start()
                vehicle.travel(80)
                vehicle.stop()
        print()
    
    def total_mileage(self):
        total_mileage = sum(vehicle.mileage for vehicle in self.vehicles)
        print("=== Total mileage of the entire park ===")
        print(f"Total mileage of all vehicles: {total_mileage} km.")

def main():
    park = TransportPark()
    
    car = Car("Toyota", "Camry", 2020)
    bicycle = Bicycle("Mountain", "Stels", 2022)
    motorcycle = Motorcycle("Harley-Davidson", "Fat Boy", 2021)
    
    park.add_vehicle(car)
    park.add_vehicle(bicycle)
    park.add_vehicle(motorcycle)
    
    park.show_all_vehicles()
    park.test_drive()
    park.total_mileage()

if __name__ == "__main__":
    main()
