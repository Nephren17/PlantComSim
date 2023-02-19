class Plant:
    def __init__(self,x,y,r=3) -> None:
        self.x = x
        self.y = y
        self.r = r
        self.name = ""
        self.t_min=0
        self.t_max=0
        self.h_min=0
        self.h_max=0
        self.l_min=0
        self.l_max=0
        self.life=0
        self.water=0
        self.water_max=0
        self.repro_period=0
        self.repro_eff=0
        self.color=""
        pass

    def __lt__(self, other):
        # 比较运算符
        return (self.x, self.y) < (other.x, other.y)
        
    def __sub__(self, other):
        # 计算距离
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        
    def __getitem__(self, index):
        # 索引器
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("MyPoint 只包含两个坐标值。")
    
    def __len__(self):
        return 2

class Cactus(Plant):   #仙人掌
    def __init__(self, x, y, r=3) -> None:
        super().__init__(x, y, r)
        self.name="Cactus"
        self.t_min=4
        self.t_max=45
        self.h_min=0.2
        self.h_max=0.4
        self.l_min=2000
        self.l_max=8000
        self.life=1000
        self.water=1500
        self.water_max=1500
        self.repro_period=40
        self.water_consume=30
        self.soil_consume=30
        self.color="#6abe83"

class Hippophae(Plant):  #沙棘 
    def __init__(self, x, y, r=3) -> None:
        super().__init__(x, y, r)
        self.name="Hippophae"
        self.t_min=-40
        self.t_max=40
        self.h_min=0.2
        self.h_max=0.8
        self.l_min=1000
        self.l_max=2000
        self.life=150
        self.water=100
        self.water_max=100
        self.repro_period=20
        self.water_consume=3
        self.soil_consume=3
        self.color="#F78D3F"

class Thorn(Plant):  #荆条
    def __init__(self, x, y, r=3) -> None:
        super().__init__(x, y, r)
        self.name="Thorn"
        self.t_min=-20
        self.t_max=30
        self.h_min=0.4
        self.h_max=0.8
        self.l_min=2000
        self.l_max=60000
        self.life=150
        self.water=100
        self.water_max=100
        self.repro_period=20
        self.water_consume=3
        self.soil_consume=3
        self.color="#393939"



# Plant suitable for Tropical savanna and temperate grassland
class Stipa(Plant):   #针茅
    def __init__(self, x, y, r=3) -> None:
        super().__init__(x, y, r)
        self.name="Stipa"
        self.t_min=-25
        self.t_max=40
        self.h_min=0.1
        self.h_max=0.8
        self.l_min=1500
        self.l_max=5000
        self.life=100
        self.water=120
        self.water_max=120
        self.repro_period=2.5
        self.water_consume=5
        self.soil_consume=5
        self.color="#FF5A09"

class Villous_themeda(Plant):   #菅子草
    def __init__(self, x, y, r=3) -> None:
        super().__init__(x, y, r)
        self.name="Villous_themeda"
        self.t_min=-6
        self.t_max=32
        self.h_min=0.3
        self.h_max=0.7
        self.l_min=1000
        self.l_max=4000
        self.life=100
        self.water=120
        self.water_max=120
        self.repro_period=4
        self.water_consume=5
        self.soil_consume=5
        self.color="#00303F"


# Plant suitable for Temperate grassland
class Arteannuin(Plant):  #黄花蒿 
    def __init__(self, x, y, r=3) -> None:
        super().__init__(x, y, r)
        self.name="Arteannuin"
        self.t_min=-20
        self.t_max=35
        self.h_min=0.3
        self.h_max=0.8
        self.l_min=500
        self.l_max=2000
        self.life=200
        self.water=150
        self.water_max=150
        self.repro_period=3
        self.water_consume=6
        self.soil_consume=6
        self.color="#7A9D96"



class Poplar(Plant):  #胡杨
    def __init__(self, x, y, r=3) -> None:
        super().__init__(x, y, r)
        self.name="Poplar"
        self.t_min=-30
        self.t_max=40
        self.h_min=0.15
        self.h_max=0.7
        self.l_min=500
        self.l_max=2000
        self.life=16000
        self.water=9000
        self.water_max=9000
        self.repro_period=10000000
        self.water_consume=150
        self.soil_consume=120
        self.color="#F6C325"

class Argy(Plant):  #艾草
    def __init__(self, x, y, r=3) -> None:
        super().__init__(x, y, r)
        self.name="Argy"
        self.t_min=-15
        self.t_max=35
        self.h_min=0.4
        self.h_max=0.7
        self.l_min=400
        self.l_max=2500
        self.life=100
        self.water=100
        self.water_max=100
        self.repro_period=4
        self.water_consume=5
        self.soil_consume=5
        self.color="#FA8072"


class Crofton_weed(Plant):  #紫茎泽兰
    def __init__(self, x, y, r=3) -> None:
        super().__init__(x, y, r)
        self.name="Crofton_weed"
        self.t_min=-5
        self.t_max=30
        self.h_min=0.3
        self.h_max=0.8
        self.l_min=1000
        self.l_max=5000
        self.life=140
        self.water=120
        self.water_max=120
        self.repro_period= 1.2
        self.water_consume=8
        self.soil_consume=8
        self.color="#7FFFD4"

class Leymus_chinensis(Plant):  #羊草
    def __init__(self, x, y, r=3) -> None:
        super().__init__(x, y, r)
        self.name="Leymus_chinensis"
        self.t_min=-20
        self.t_max=35
        self.h_min=0.3
        self.h_max=0.8
        self.l_min=500
        self.l_max=2000
        self.life=100
        self.water=100
        self.water_max=100
        self.repro_period=4
        self.water_consume=5
        self.soil_consume=5
        self.color="#800080"


class Locust(Plant):  #刺槐
    def __init__(self, x, y, r=3) -> None:
        super().__init__(x, y, r)
        self.name="Locust"
        self.t_min=-25
        self.t_max=35
        self.h_min=0.3
        self.h_max=0.8
        self.l_min=500
        self.l_max=3000
        self.life=14000
        self.water=15000
        self.water_max=15000
        self.repro_period=6
        self.water_consume=150
        self.soil_consume=150
        self.color="#FF00FF"

# Plant that is suitable for all the three  types of climate

class Chinese_pennisetum(Plant):  #狼尾草
    def __init__(self, x, y, r=3) -> None:
        super().__init__(x, y, r)
        self.name="Chinese_pennisetum"
        self.t_min=-15
        self.t_max=35
        self.h_min=0.3
        self.h_max=0.7
        self.l_min=3000
        self.l_max=60000
        self.life=100
        self.water=100
        self.water_max=100
        self.repro_period=6
        self.water_consume=5
        self.soil_consume=5
        self.color="#8F00FF"

class Conyza_canadensis(Plant):  #飞蓬
    def __init__(self, x, y, r=3) -> None:
        super().__init__(x, y, r)
        self.name="Conyza_canadensis"
        self.t_min=-10
        self.t_max=35
        self.h_min=0.2
        self.h_max=0.7
        self.l_min=500
        self.l_max=2000
        self.life=100
        self.water=100
        self.water_max=100
        self.repro_period=6
        self.water_consume=6
        self.soil_consume=6
        self.color="#00FFFF"


cac = Cactus(2,3)
print(cac.l_min)