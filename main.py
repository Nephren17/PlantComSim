import numpy as np
from plantclass import *
from world import *
import random
from scipy.spatial import KDTree
import matplotlib.pyplot as plt
import kdtree
from init import *
from waether_sim import simulate_tropical_savanna_climate_daily
from helper_func import *


temperature,humidity,_ = simulate_tropical_savanna_climate_daily()
world=init(300)
tik = 0

temp_hp_loss=0
hum_hp_loss=0

def plant_itr(plant:Plant):
    sec = plant.get_sec()      # 返回索引
    section = world.sections[sec]
    neighbors = section.plants
    plant.life = HealthPointIteration(plant,section,neighbors)
    plant.water = WaterPointIteration(plant,section,neighbors)
    if plant.water < 60 :
        plant.life = plant.life + plant.water - 60

def plants_iteration():
    for plant in world.plants:
        plant_itr(plant)
        if plant.age_() == False:
            world.plants.remove(plant)
    #print("At time " + str(tik) + " there are " + str(len(world.plants)) + " left")
        

def sec_itr(section:Section,climate:Climate):
    section.sil_hum=SoilHumidityIteration(section=section,climate=climate)

world.vis(fname="start",collection=["Cactus","Hippophae","Thorn","Stipa"])
year = 1
while 1:

    climate = Climate(temperature[tik],humidity[tik])
    plants_iteration()
    for section in world.sections:
        sec_itr(section,climate)




    #world.update_sec()

    tik = tik + 1

    if tik == 10:
        world.vis(fname="10",collection=["Cactus","Hippophae","Thorn","Stipa"])

    if tik == 20:
        world.vis(fname="20",collection=["Cactus","Hippophae","Thorn","Stipa"])

    if tik == 26:
        world.vis(fname="26",collection=["Cactus","Hippophae","Thorn","Stipa"])

    if tik == 27:
        world.vis(fname="27",collection=["Cactus","Hippophae","Thorn","Stipa"])

    if tik == 28:
        world.vis(fname="28",collection=["Cactus","Hippophae","Thorn","Stipa"])

    if tik == 30:
        world.vis(fname="30",collection=["Cactus","Hippophae","Thorn","Stipa"])

    if tik == 29:
        world.vis(fname="29",collection=["Cactus","Hippophae","Thorn","Stipa"])
    
    
    if tik > 300 or len(world.plants)==0 :
        break

world.vis(fname="final",collection=["Cactus","Hippophae","Thorn","Stipa"])



    
    

