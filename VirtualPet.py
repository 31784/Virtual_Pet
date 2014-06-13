class VirtualPet:
    """An implementation of a Virtual pet"""
    #contructor method
    def __init__(self,name):
        #attributes
        self.name=name
        self.hunger= 50
        print("Hi,I've been born and I am called {0}".format(name))

            #methods        
    def talk(self):
        print("Hello I am your new pet")

    def eat(self,Feed):
        if Feed == "1":
            self.hunger=self.hunger - 20
        elif Feed == "2":
            self.hunger=self.hunger - 10
        self.hunger=self.hunger + 10
        
def DisplayMenu():
    print()
    print('MENU')
    print()
    print('1. Feed pet')
    print()
    print('Select an option from the menu (or enter q to quit simulation): ', end='')

def GetMenuChoice():
    Choice = input()
    print()
    return Choice.lower()[0]

def Feed():
    Feed=input("What would you like to feed? (1 for Bannana, 2 for chocolate, anything else to not feed): ")
    if Feed == "1":
        print("yummy bannana")
    elif Feed == "2":
        print("CHOCOLATE I LOVE YOU!!!")
    else:
        print("But why do you not want to feed me :(")

def main():
    name=input("What do you want to call your pet: ")
    #instantiation
    pet_one=VirtualPet(name)
    #call the talk method
    pet_one.talk()
    Choice = ''
    while Choice != 'q':
        DisplayMenu()
        Choice = GetMenuChoice()
        if Choice == '1':
            Feed()
        else:
            print("End simulation")
    
if __name__=="__main__": 
    main()

        
