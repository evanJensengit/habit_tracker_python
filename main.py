
class Week:
    workout = 0
    sleep = 0
    meditate = 0
    stretch = 0
    calls = 0
    sugar = 0
    pci = 0
    def __init__(self):
        self.workout = 0
        self.sleep = 0
        self.meditate = 0
        self.stretch = 0
        self.calls = 0
        self.sugar = 0
        self.pci = 0
        
    # Date: str
    # Workout: str
    # Sleep: str
    # Meditate: str
    # Stretch: str
    # Calls: int
    # Sugar: str
    # PCI: int

def processWeek(lines):

    week = Week()
    for line in lines: 
        if not line:
            words = line.split(":")
            print(words[1])
    return week


    
f = open('pci.txt','r')

lines = []

with open('pci.txt') as f:
    lines = f.readlines()
word = []

count = 0
week = processWeek(lines)
print(week)
