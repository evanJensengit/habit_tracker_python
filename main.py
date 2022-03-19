
workout = "Wrkt"
sleep = "Sleep"
meditate = "Meditate"
stretch = "Stretch"
calls = "Calls"
sugar = "<20 g sugar"
pci = "PCI"
caffeine = "<300 mg caff"
class Week:
    workout = 0
    sleep = 0
    meditate = 0
    stretch = 0
    calls = 0
    sugar = 0
    pci = 0
    caffeine = 0
    def __init__(self):
        return

    #increments number of week object data members based on data in lines list
    def processWeek(self, lines):
        
        for line in lines: 
            
            words = line.split(":") #get description of item to be tracked and value of that item
            
            if len(words) > 1: #there is something in the line
                descript = words[0]
                
                yesorno = words[1]

               
                # for word in words:
                #     print(word,end='')
               
                if descript == workout and yesorno[1]== "y":
                    self.workout += 1
                elif descript == pci:
                    self.pci += int(yesorno[1])
                elif descript == calls:
                    self.calls += int(yesorno[1])
                elif descript == meditate:
                    if (yesorno[1] == "y"):
                        self.meditate += 1
                elif descript == stretch:
                    if (yesorno[1] == "y"):
                        self.stretch += 1
                elif descript == sugar:
                    if (yesorno[1] == "y"):
                        self.sugar += 1
                elif descript == caffeine:
                    if (yesorno[1] == "y"):
                        self.caffeine += 1
                elif descript == sleep:
                    if (yesorno[1] == "y"):
                        self.sleep += 1

            
        return
    def printWeek(self):
        print("Last 7 days stats and PCI:")
        print("  Total workouts:   ", self.workout)
        print("  8 hours sleep:    ", self.sleep)
        print("  Meditated:        ", self.meditate)
        print("  Stretched:        ", self.stretch)
        print("  Sugar < 20 g:     ", self.sugar)
        print("  Caffeine < 300 mg:", self.caffeine)
        print("  Calls:            ", self.calls)
        print("  PCI score:        ", self.pci)


    
f = open('pci.txt','r')

lines = []

with open('pci.txt') as f:
    lines = f.readlines()
week = Week()
week.processWeek(lines)
print()
week.printWeek()
