
workout = "Wrkt"
sleep = "Sleep"
meditate = "Meditate"
stretch = "Stretch"
calls = "Calls"
sugar = "Sugar"
pci = "PCI"
class Week:
    workout = 0
    sleep = 0
    meditate = 0
    stretch = 0
    calls = 0
    sugar = 0
    pci = 0
    def __init__(self):
        return

    def processWeek(self, lines):
        
        for line in lines: 
            words = line.split(":")
            if len(words) > 1:
                print(words[1],end='')
                
                if len(words) == 2:
                   YornAndType = words[1].split(" ")
                else:
                    YornAndType = words[1]
                if words[0] == "Wrkt" and YornAndType[1]=="y":
                    self.workout += 1

            
        return
    def printWeek(self):
        print(self.workout)
        print(self.sleep)
        print(self.meditate)
        print(self.stretch)
        print(self.calls)
        print(self.sugar)
        print(self.pci)

    
f = open('pci.txt','r')

lines = []

with open('pci.txt') as f:
    lines = f.readlines()
week = Week()
week.processWeek(lines)
week.printWeek()
