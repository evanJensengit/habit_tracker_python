
class Day:
    def __init__(date, workout, sleep, meditate, stretch, calls, sugar, pci)
    self.date = date
    self.workout = workout
    self.sleep = sleep
    self.meditate = meditate
    self.stretch = stretch
    self.calls = calls
    self.sugar = sugar
    self.pci = pci
    # Date: str
    # Workout: str
    # Sleep: str
    # Meditate: str
    # Stretch: str
    # Calls: int
    # Sugar: str
    # PCI: int


    
f = open('pci.txt','r')

lines = []

with open('pci.txt') as f:
    lines = f.readlines()
word = []
dayObjects = []
listWithDayObjectsRaw = []
count = 0
for line in lines:
    if not line:
        createDay(listWithDayObjectsRaw,)
    word = line.split(":")
    listWithDayObjectsRaw.append(word)
    
    print(line)

