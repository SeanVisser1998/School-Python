class Vehicle:
    def __init__(self, id, location):
        self.id = id
        self.location = location
        self.target_location = (-1, -1)

    def set_target_location(self, target_location):
        self.target_location = target_location

    def pickup(self, passenger):
        pass

class Taxi(Vehicle):
    def __init(self, id, location):
        super(Taxi, self).__init__(id, location)
        
    def set_target_location(self, target_location):
        self.target_location = target_location 

    def pickup(self, passenger):
        self.passenger = passenger
        self.set_target_location(passenger.target_location) #Set de target_location naar de locatie van de passenger :)
    

class Minibus(Vehicle):
    def __init(self, id, location):
        super(Minibus, self).__init__(id, location)
        
    def set_target_location(self, target_location):
        self.target_location = target_location     
           
    def pickup(self, passenger):
        self.set_target_location(passenger.target_location) #Set de target_location naar de locatie van de passenger :)
    

class TaxiCompany:
    def __init__(self):
        self.vehicles = []
        self.assignments = {} # k,v = (vehicle_id, passenger_name)

    def register(self, vehicle):
        self.vehicles.append(vehicle)

    def request_pickup(self, passenger):
        vehicle = self.schedule_vehicle(passenger) #Scheduled een vehicle voor een passenger =)
        if vehicle: #Als vehicle TRUE is...
            self.assignments[vehicle.id] = passenger.name #Koppelt de vehicle aan de passenger :)
            vehicle.pickup(passenger) #Stuurt de vehicle om de klant op te halen
            return True #Geeft True terug (Heeft te maken met als die en keer op False komt dat ie dan ook weer op True kan komen :3
        else:
            return False #NEEE, GEEN TAXI BESCHIKBAAR BLYAT

    def schedule_vehicle(self, p):
        for v in self.vehicles:
            if v.target_location == (-1,-1):
                if abs(v.location[0] - p.location[0]) < 10 and abs(v.location[1] - p.location[1]) < 10:
                    return v
    
class Passenger:
    def __init__(self, name, location, target_location):
        self.name = name
        self.location = location
        self.target_location = target_location

# main
tc = TaxiCompany()
t1 = Taxi('blyat1', (1, 1))
t2 = Taxi('blyat2', (2, 2))
m1 = Minibus('cyka1', (3, 3))
m2 = Minibus('cyka2', (4, 4))

tc.register(t1)
tc.register(t2)
tc.register(m1)
tc.register(m2)

p1 = Passenger('Vadim', (4,4), (5,0))
p2 = Passenger('Ivan', (5,5), (6,0))
p3 = Passenger('Igor',  (2,2), (7,0))
p4 = Passenger('Svetlana', (11,3), (7,0))
p5 = Passenger('Tanja',  (13,8), (7,0))

for p in (p1, p2, p3, p4, p5):
    if tc.request_pickup(p):
        print(p.name, 'is met Boris Taxi Company BLYAT opgehaald ofzo')
    else:
        print('Boris Taxi Company BLYAT is bezig, FUCK YOU', p.name)

for v, p in tc.assignments.items():
    print(p, "is in de", v)