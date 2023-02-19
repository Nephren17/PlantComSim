import matplotlib.pyplot as plt
from waether_sim import simulate_tropical_savanna_climate_daily
from typing import List
from plantclass import Plant
temperature,humidity,_ = simulate_tropical_savanna_climate_daily()
class Section:
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y
        self.tem=temperature[0]
        self.hum=humidity[0]
        self.sil_hum=10000
        self.nut=100
        self.plants=[]
        self.density=0
        
    def get_density(self):
        return self.plants.__len__() 

    def add_plant(self,plant):      
        if (plant.x >= self.x*10 and plant.x < self.x*10 + 10 and plant.y >= self.y*10 and plant.y < self.y*10 + 10):
            self.plants.append(plant)
        self.density=self.density + 1

    def add_plants(self,plants):         #筛选并将符合条件的植物放入网格
        for plant in plants:
            self.add_plant(plant)

    def len(self):
        return self.plants.__len__()

    def print(self):
        if self.len() == 0:
            print("Sec(" + str(self.x) + ","+ str(self.y) + ") is empty") 
            return
        print("In Sec(" + str(self.x) + ","+ str(self.y) + ")")
        for plant in self.plants:
            print(plant.name +" " + str(plant.x) + " " + str(plant.y) + ";")


class World:
    def __init__(self,plants:List[Plant],rows=100,cols=100) -> None:
        self.rows=rows
        self.cols=cols
        self.time=0
        self.presp=0
        self.tem_avg=0
        self.tem_diff=0
        self.sunlight=0
        self.humidity=0
        self.plants=plants
        self.sections=[]
        for i in range(0,10):
            for j in range(0,10):
                self.sections.append(Section(i,j))

    def update_sec(self):     #更新各个网格中的植物信息
        self.sections=[]
        for i in range(0,10):
            for j in range(0,10):
                self.sections.append(Section(i,j))
        for sec in self.sections:
            sec.add_plants(self.plants)

    def debug_sec(self,x:int,y:int):
        sec = self.sections[x*10 + y]
        sec.print()

    def vis(self,fname="distribution",line=False,collection=["Cactus","Hippophae","Thorn","Stipa"]):
        plt.figure(dpi=300).set_size_inches(10,8)
        for plant in self.plants:
            if plant.name in collection:
                plt.scatter(plant.x,plant.y,c=plant.color,label=plant.name)
                collection.remove(plant.name)
            else:
                plt.scatter(plant.x,plant.y,c=plant.color)

        if line == True:
            for i in range(0,10):
                plt.axhline(y=i*10,color='#d9d9f3', linestyle='--')
                plt.axvline(x=i*10,color='#d9d9f3', linestyle='--')

        plt.title("Distribution")
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left') 
        plt.xlim(0,100)
        plt.ylim(0,100)
        ax = plt.gca()
        ax.set_aspect('equal')
        plt.show()
        plt.savefig(fname)
