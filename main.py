#Location Finder Class
class LocationFinder:

    def __init__(self):
        self.locations = {}

    def update(self, item, location):
        self.locations[item] = location

    def where(self, item):
        #To avoid KeyError exceptions, using get rather than []
        loc = self.locations.get(item)
        if loc != None:
            return f"{item} : " + loc
        else:
            return f"{item} : Unknown Location"

#Testing
lf = LocationFinder()
lf.update("Dance Shoes", "Basement")
lf.update("Tent", "Garage")
lf.update("Passport", "Safe")

print(lf.where("Dance Shoes"))
print(lf.where("Tent"))
#Test case without location
print(lf.where("Phone"))
