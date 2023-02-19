class Section:
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y
        self.hum=30
        self.sil_hum=30
        self.nut=100
        self.plants=[]
        
    def add_plant(self,plant):      
        if (plant.x >= self.x*10 and plant.x < self.x*10 + 10 and plant.y >= self.y*10 and plant.y < self.y*10 + 10):
            self.plants.append(plant)

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
    def __init__(self,plants,rows=100,cols=100) -> None:
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
