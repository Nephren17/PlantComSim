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
world=init(100)
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
        plant.age_()

def sec_itr(section:Section,climate:Climate):
    section.sil_hum=SoilHumidityIteration(section=section,climate=climate)

    

while 1:
    climate = Climate(temperature[tik],humidity[tik])
    plants_iteration()
    for section in world.sections:
        sec_itr(section,climate)




    #world.update_sec()

    tik = tik + 1
    if tik == 50:
        world.vis(line=True)
    if tik == 100:
        world.vis(line=True)
    if tik == 150:
        world.vis(line=True)
    if tik == 200:
        world.vis(line=True)
    if tik == 250:
        world.vis(line=True)
    if tik > 300:
        break

world.vis(line=True)

