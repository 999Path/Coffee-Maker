'''
Name: Min Soonthornsawat
Assignment 10.1 : Your Own Class

'''
class coffee_machine: 
    hot = True
    def __init__(self,types,shots):
        # default the shots,milk foam and steam milk
        self.shots = shots
        # If shots = string, set the shots to 0
        if type(shots) == str: 
            print("Shots cannot be a string, or else it will be set to default")
            self.shots = 0
        self.type = types 
        self.__milk_foam = False
        self.__steam_milk = 0
        
        # if type = espresso, set default add one more shot
        if types == "Espresso":
                self.shots += 1
        
        # if type = espresso macchiato, set default add one more shot and set Milk foam to True
        elif types == "Espresso Macchiato":
                self.shots += 1
                self.__milk_foam = True

        # if type = latte, set default add one more shot, two more steam milk and set milk foam to True
        elif types == "Latte":
                self.shots += 1
                self.__steam_milk += 2
                self.__milk_foam = True

    def venti_size(self):
        # change the shot and milk quantity by two times
        self.shots = self.shots * 2
        self.__steam_milk * 2
    
    def grande_size(self):
        # change the shot and milk quantity deducting by two times
        self.shots = self.shots / 2
        self.__steam_milk /2

    def set_foam(self,foam):
        # set amount of milk foam to True or False
        if foam == False:
            self.__milk_foam = False 
        elif foam == True: 
            self.__milk_foam = True 
        else: 
        # if input is something else, prompt the user to change the input
            print("The input have to be True or False")
    
    def set_steamed_milk(self,steam):
        if steam < 0: 
        # if the input of steam is lesser than 0, print out the following:
            print("Steam milk request can't be less than zero, if less than zero, we will respectfully break your cup.")
        elif steam > 0: 
        # elif, set the steam to the input
            self.__steam_milk = steam
        else:
        # else prompt the user to change the input
            print("Input have to be a float or integer")
    
    def get_steam_milk(self):
        return self.__steam_milk
    
    def get_foam(self):
        return self.__milk_foam
    
    def __str__(self):
    # Magic method
    # Return what the machine is making.
        return (f"Making: Type - {self.type} (Ingredients: shots - {self.shots}, Milk foam- {self.__milk_foam}, Steam milk - {self.__steam_milk})")

# Testing the code
def main():
    latte = coffee_machine("Latte","LOL")
    print(latte)
    latte = coffee_machine("Latte",4)
    none = coffee_machine("None",2)
    none.set_steamed_milk(-1)
    none.set_foam(True)
    print(none)
    none.venti_size()
    print(none)

if __name__ == "__main__":
    main()



