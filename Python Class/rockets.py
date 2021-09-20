################################################################################
# Author: Migul Castilho Oliveira
# Date: 04/22/2021
# Description calculates the cost for rockets. It uses two different classes and inheritance to overide methods
################################################################################

class Rocket():
    #Defining the rocket class, with all of the attributes necessary
    def __init__(self, name, booster_cost, upper_stage_cost, fuel_cost):
        self.name = name
        self.booster_cost = booster_cost
        self.upper_stage_cost = upper_stage_cost
        self.fuel_cost = fuel_cost
        #instantiation
    #Defining the first method of cost per launch
    def cost_per_launch(self):
        costLaunch = self.booster_cost + self.upper_stage_cost + self.fuel_cost
        return(costLaunch)
        
class ReusableRocket(Rocket):
    #Here we inherit and overide the roket class by adding a "uses" attribute.
    def __init__(self, name, booster_cost, upper_stage_cost, fuel_cost, uses):
        self.uses = uses
        super().__init__(name, booster_cost, upper_stage_cost, fuel_cost)
    
    #overiding the method by changing it
    def cost_per_launch(self):
        reusableCost = (self.booster_cost / self.uses) + self.upper_stage_cost + self.fuel_cost
        return(reusableCost)


def main():
    #defining the classes to variables to they store the respective rockets
    atlasV = ReusableRocket("Atlas V", 65.4, 42.6, 0.23, 1)
    
    ariane5 = ReusableRocket("Ariane 5", 83.5,55.6, 0.69, 1)
    
    longMarch = ReusableRocket("Long March 3B", 28.5, 19.0, 2.38, 1)
    
    soyuz2 = ReusableRocket("Soyuz 2", 20.9, 13.9, 0.24, 1)
    
    falcon9 = ReusableRocket("Falcon 9", 43.0, 18.6, 0.45, 10)
    #determine the costs to the respective rockets
    costAtlas = atlasV.cost_per_launch()
    
    costAriane = ariane5.cost_per_launch()
    
    costMarch = longMarch.cost_per_launch()
    
    costSoyuz = soyuz2.cost_per_launch()
    
    costFalcon = falcon9.cost_per_launch()
    #printing it all
    print(f"This Atlas V cost ${costAtlas:0.2f} million per launch.")
    print(f"This Ariane 5 cost ${costAriane:0.2f} million per launch.")
    print(f"This Long March 3B cost ${costMarch:0.2f} million per launch.")
    print(f"This Soyuz 2 cost ${costSoyuz:0.2f} million per launch.")
    print(f"This Falcon 9 cost ${costFalcon:0.2f} million per launch.")  

if __name__ == '__main__':
    main()
