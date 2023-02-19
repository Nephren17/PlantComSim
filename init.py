import numpy as np
from plantclass import *
from world import *
import random
from scipy.spatial import KDTree
import matplotlib.pyplot as plt
import kdtree

def generate_points(n, radius=2):
    # 随机生成第一个点
    x = random.uniform(radius, 100 - radius)
    y = random.uniform(radius, 100 - radius)
    points = [(x, y)]
    
    while len(points) < n:
        # 随机生成下一个点的位置
        x = random.uniform(radius, 100 - radius)
        y = random.uniform(radius, 100 - radius)
        point = (x, y)
        
        # 计算与最近的点的距离
        kdtree = KDTree(points)
        dist, _ = kdtree.query(point)
        
        # 如果距离太小，则重新生成点
        if dist < radius:
            continue
        
        # 将点添加到列表中
        points.append(point)
    
    return points

def gen_plant(n,point,r=3):
    x=point[0]
    y=point[1]
    if n==1:
        plant=Cactus(x,y)
    elif n==2:
        plant=Arteannuin(x,y)
    elif n==3:
        plant=Hippophae(x,y)
    elif n==4:
        plant=Poplar(x,y)
    else:
        plant=Cactus(x,y)
    
    return plant

def vis(plants,line=False):
    plt.figure(dpi=300).set_size_inches(7,7)
    for plant in plants:
        plt.scatter(plant.x,plant.y,c=plant.color,label=plant.name)
    if line == True:
        for i in range(0,10):
            plt.axhline(y=i*10,color='#d9d9f3', linestyle='--')
            plt.axvline(x=i*10,color='#d9d9f3', linestyle='--')

    plt.title("Distribution")
    #plt.legend()
    plt.xlim(0,100)
    plt.ylim(0,100)
    ax = plt.gca()
    ax.set_aspect('equal')
    plt.savefig("distribution.png")



points = generate_points(50)  # generate 50 random plants
plants=[]
for point in points:
    idx = np.random.randint(1,5)
    plant = gen_plant(idx,point,2)
    plants.append(plant)
plant_tree = kdtree.create(plants)  #kdtree 数据结构存储plant信息，便于计算相隔距离

world = World(plants=plants)
world.update_sec()
world.debug_sec(0,0)
vis(plants=plants,line=True)


