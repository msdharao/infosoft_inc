class FuelStation:
    def __init__(self,diesel:int, petrol:int, electric:int):
        self.diesel: int = diesel
        self.petrol : int = petrol
        self.electric : int = electric
        self.diesel1: int = diesel
        self.petrol1 : int = petrol
        self.electric1 : int = electric

    def fuel_vehicle(self, fuel_type:str)-> bool:
        if fuel_type == "diesel":
            if self.diesel == 0:
                return False
            else:
                self.diesel = self.diesel-1
                return True
        elif fuel_type == "petrol":
            if self.petrol == 0:
                return False
            else:
                self.petrol =  self.petrol-1
                return True
        elif fuel_type == "electric":
            if self.electric == 0:
                return False
            else:
                self.electric =  self.electric-1
                return True
        return False

    def open_fuel_slot(self, fuel_type:str)-> bool:
        if fuel_type == "diesel":
            if self.diesel < self.diesel1:
                self.diesel = self.diesel + 1
                return True
            else:
                return False
        elif fuel_type == "petrol":
            if self.petrol < self.petrol1:
                self.petrol = self.petrol+1
                return True
            else:
                return False
        elif fuel_type == "electric":
            if self.electric < self.electric1:
                self.electric = self.electric + 1
                return True
            else:
                return False
        return False

fuel_station = FuelStation(diesel=2, petrol=2, electric=1)
fuel_station.fuel_vehicle("diesel")
fuel_station.fuel_vehicle("petrol")
fuel_station.fuel_vehicle("diesel")
fuel_station.fuel_vehicle("electric")
fuel_station.fuel_vehicle("diesel")
fuel_station.open_fuel_slot("diesel")
fuel_station.fuel_vehicle("diesel")
fuel_station.open_fuel_slot("electric")
fuel_station.open_fuel_slot("electric") 
