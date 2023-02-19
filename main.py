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
import pickle


temperature,humidity,_ = simulate_tropical_savanna_climate_daily()

total=300
plant_list = [1]*int(total*0.7) + [2]*int(total*0.1) + [3]*int(total*0.1) + [4]*int(total*0.1)

world=init(total)
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

world.vis(fname="start",collection=["Cactus","Hippophae","Poplar","Stipa","Argy"])
year = 1
log = []
while 1:

    climate = Climate(temperature[tik%360],humidity[tik%360])
    plants_iteration()
    for section in world.sections:
        sec_itr(section,climate)

    world.update_sec()

    tik = tik + 1

    if tik == 100:
        world.vis(fname="100",collection=["Cactus","Hippophae","Poplar","Stipa","Argy"])
        with open('possibility.txt', 'w') as file:
            file.write(str(len(world.plants)/total)+" at day 100\n")

    if tik == 200:
        world.vis(fname="200",collection=["Cactus","Hippophae","Poplar","Stipa","Argy"])
        with open('possibility.txt', 'a') as file:
            file.write(str(len(world.plants)/total)+" at day 200\n")

    log.append(len(world.plants)/total)
    if tik > 800 or len(world.plants)==0 :
        break


world.vis(fname="final",collection=["Cactus","Hippophae","Poplar","Stipa","Argy"])
with open('possibility.txt', 'a') as file:
    file.write(str(len(world.plants)/total)+" at day 300\n")

x_ax = range(0,len(log))

plt.figure(dpi=300).set_size_inches(8,6)
plt.plot(x_ax,log)
plt.xlabel("day")
plt.ylabel("survival possibility")
plt.ylim(0,1.05)
#plt.xlim(0,300)
plt.savefig("log.png")

#with open('data5.pkl', 'ab') as f:
 #   pickle.dump(log, f)













def test_comp(plant_list):
    world=init_sp(plant_list)
    tik = 0   
    log = []
    while 1:

        climate = Climate(temperature[tik],humidity[tik])
        plants_iteration()
        for section in world.sections:
            sec_itr(section,climate)
        
        world.update_sec()

        tik = tik + 1

        log.append(len(world.plants)/total)
        if tik > 300 or len(world.plants)==0 :
            break
    
    return log

