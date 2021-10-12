class Brother:
    '''Class to represent a brother of Chi Phi '''
        
    def __init__(self, name, year, floor=0):
        
        self.name = name
        self.year = year
        self.floor = floor
        self.weight = 0
        
    def getName(self):
        return self.name
        
    def getYear(self):
        return self.year
    
    def getFloor(self):
        return self.floor
    
    def getWeight(self):
        return self.weight
    
    def setWeight(self, newWeight):
        self.weight = newWeight
        
    def __str__(self):
        return self.getName()
        

seniors = [
    #Brother('Pablo Ampudia', 4),
    #Brother('Will Nash', 4),
    #Brother('John Paris', 4),
    Brother('Adam Katz', 4, 5),
    #Brother('Collin Renae', 4, 4),
    Brother('Giovanni Ahern', 4, 4),
    Brother('Fiyi Adebekun', 4, 4),
    Brother('Kyri Chen', 4, 4),
    Brother('Brian Glat', 4, 4),
    Brother('Cooper Jones', 4, 4),
    Brother('Ian Merrick', 4, 4),
    Brother('Liam Miller', 4, 4),
    Brother('James Santoro', 4, 4),
    Brother('Jonah Scott', 4, 4)
]

juniors = [
    #Brother('Andrew Johnson', 3, 3),
    Brother('Andrew Palleiko', 3, 5),
    Brother('Benji Grossman', 3, 3),
    Brother('Brady Darby', 3, 3),
    Brother('Chris Perrino', 3, 5),
    Brother('Teddy Corcoran', 3, 5),
    Brother('Erik Anderson', 3, 3),
    Brother('Graham Cartwright', 3, 3),
    Brother('Hudson Hooper', 3, 3),
    Brother('James Richardson', 3, 5),
    Brother('Jared Boisvert', 3, 3),
    Brother('Kyle Sonandres', 3, 3),
    #Brother('Matthew Nay', 3, 3),
    Brother('Nick Gustafson', 3, 3),
    Brother('Prosser Cathey', 3, 4),
    Brother('Sam Costa', 3, 4),
    Brother('Sawyer Koetters', 3, 3),
    Brother('Teddy Schoenfeld', 3, 5),
    Brother('Tyler Kim', 3, 3)
]

sophomores = [
    Brother('Alonso Garcia', 2, 3),
    Brother('Anthony Altala', 2, -1),
    Brother('Heath Nilsen', 2, 3),
    Brother('Jack McCordic', 2, 4),
    Brother('Joseph Chandler', 2, 5),
    Brother('Joey Lupo', 2, 5),
    Brother('Karl Meyer', 2, 5),
    Brother('Luke Chapman', 2, 5),
    Brother('Mike Hadjiivanov', 2, 3),
    Brother('Peter Detolla', 2, 4),
    Brother('Ryan Armstrong', 2, 4),
    Brother('Ryan Welch', 2, 3),
    Brother('Stan Lacksen', 2, 3),
    Brother('Teague Rice', 2, 5)
]

freshmen = [
    Brother('Nico Bowden', 1),
    Brother('Dylan Nelson', 1),
    Brother('Brian Rapanan', 1),
    Brother('Dusan Cvetkovic', 1),
    Brother('Isaac Villalobos', 1),
    Brother('Josh Callaway', 1),
    Brother('Malachi Soqui', 1),
    Brother('Matt Sardis', 1)
]