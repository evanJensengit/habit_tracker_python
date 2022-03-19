
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

    #increments number of week object data members based on data in lines list
    def processWeek(self, lines):
        
        for line in lines: 
            
            words = line.split(":") #get description of item to be tracked and value of that item

            if len(words) > 1: #there is something in the line
                descript = words[0]
                YornAndType = []

                if len(words) > 2: 
                   YornAndType = words[1].split(' ') #get the y and other data 
                else:
                    YornAndType.append(words[1]) #no type 

                # for word in words:
                #     print(word,end='')
                count = 0
                for yorn in YornAndType:
                    
                    print(count, " ", yorn)
                    count +=1
                #print("hi" + YornAndType[0],end='')
                if descript == workout and words[1][1]=="y":
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
print()
week.printWeek()
