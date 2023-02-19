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
        self.color="#6abe83"

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
        self.color="#F0D879"

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
        self.color="#F78D3F"

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
        self.color="#248888"

cac = Cactus(2,3)
print(cac.l_min)