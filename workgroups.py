class Workgroup:
    '''Class to represent a workgroup for the John F. Andrews House '''

    def __init__(self, name, floor, capacity):
        self.name = name
        self.floor = floor
        self.capacity = capacity
        
    def getFloor(self):
        return self.floor
    
    def getName(self):
        return self.name
    
    def getCapacity(self):
        return self.capacity
        
    def __str__(self):
        return self.getName()
        
    
workgroups = [
    Workgroup('Laundry Room', -1, 1),
    Workgroup('Poker Room', -1, 1),
    Workgroup('Stalag', -1, 1),
    Workgroup('Basement Bathroom', -1, 1),
    Workgroup('Gym', -1, 1),
    Workgroup('Maker Space', -1, 1),
    Workgroup('Freshmen Study', 1, 1),
    Workgroup('Maidenhead', 1, 1),
    Workgroup('Foyer', 1, 2),
    Workgroup('Library', 1, 1),
    Workgroup('Pool Room', 1, 2),
    Workgroup('Main Hall', 2, 2),
    Workgroup('Dining Hall', 2, 2),
    Workgroup('Pantry', 2, 2),
    Workgroup('Gold Room', 2, 2),
    Workgroup('Music Room', 2, 1),
    Workgroup('3rd Landing', 3, 1),
    Workgroup('3rd Bathroom', 3, 1),
    Workgroup('3rd Shower', 3, 1),
    Workgroup('4th Landing', 4, 1),
    Workgroup('4th Shower', 4, 1),
    Workgroup('4th Bathroom', 4, 1),
    Workgroup('5th Hallway', 5, 1),
    Workgroup('5th Bathroom', 5, 1),
    Workgroup('Main Stairs 1-2', 2, 1),
    Workgroup('Main Stairs 2-3', 3, 1),
    Workgroup('Main Stairs 3-4', 4, 1),
    Workgroup('Back Stairs 0-3', 1, 1),
    Workgroup('Back Stairs 3-5', 1, 1)
]