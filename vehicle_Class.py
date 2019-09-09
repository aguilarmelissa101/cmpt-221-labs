##Name: Melissa Aguilar

##vehicle_Class

"""


File: vehicle_Class.py
This module defines the vehicle, electric car, and fuel car class.


"""
class gas_Vehicle (vehicle_Class):
    def __init__(self, fuel_Amount, **kwargs):
        self.fuel = fuel_Amount
        vehicle_Class.__init__(self, **kwargs)


class electric_Vehicle (vehicle_Class):
    def __init__(self, energy, **kwargs):
        self.energy_Storage = energy
        vehicle_Class.__init__(self, **kwargs):

class Vehicle_Class:
    """Represents vehicles"""
    def __init__(self, type, make, color, miles):
        """Represents all things vehicles have in common"""
        self.vehicleType = str(type)
        self.vehicleMake = str(make)
        self.vehicleColor = str(color)
        self.vehicleMiles = int(miles)

        #return self

    #Return the values of type, make, color, and miles
    def getType(self):
        """Returns the type of vehicle"""
        return self.vehicleType

    def getMake(self):
        """Returns the maker of vehicle"""
        return self.vehicleMake

    def getColor(self):
        """Returns the color of vehicle"""
        return self.vehicleColor

    def getMiles(self):
        """Returns the current amount of miles"""
        return self.vehicleMiles


    #Resets the values of type, make, color, and miles
    def setType(self):
        """Resets the type of vehicle"""
        self.vehicleType = newType

    def setMake(self):
        """Resets the maker of vehicle"""
        self.vehicleMake = newMake

    def setColor(self):
        """Resets the color of vehicle"""
        self.vehicleColor = newColor

    def setMiles(self):
        """Resets the current amount of miles"""
        return self.vehicleMiles = newMiles


    def __str__(self):
        """Returns the string representation of the vehicle"""
        vehicle = (self.vehicleType)+"\t\t"
        vehicle += (str(self.vehicleMake))+"\t\t"
        vehicle += (str(self.vehicleColor))+"\t\t"
        vehicle += (str(self.vehicleMiles))+"\t\t"
        #vehicle += (str(self.current_Fuel))+"\t\t"
        return (str(vehicle))











