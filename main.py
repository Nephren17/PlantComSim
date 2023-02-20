import numpy as np
from plantclass import *
from world import *
import random
from scipy.spatial import KDTree
import matplotlib.pyplot as plt
import kdtree
from init import *
from waether_sim import simulate_tropical_savanna_climate_daily,simulate_temperate_grassland_climate_daily
from helper_func import *
import pickle


temperature,humidity,_ = simulate_tropical_savanna_climate_daily()
total=1000
plant_list = [1]*int(total*0.5) + [2]*int(total*2) + [3]*int(total*0.2) + [4]*int(total* 0.1)

world,coef=init(total)
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
log = []
while 1:

    climate = Climate(temperature[tik%360],humidity[tik%360])
    plants_iteration()
    for section in world.sections:
        sec_itr(section,climate)
    newplants = []
    for plant in world.plants:
        if plant.age % plant.repro_period == 0:
            sec = world.sections[plant.get_sec()]
            if sec.sil_hum > 200 and sec.nut > 200 and random.random() > 0.95:
                newplants.append(spawn(plant))
                sec.sil_hum = sec.sil_hum - 100
                sec.nut = sec.nut - 100
            #print("New plant spawned!")
    world.plants = world.plants + newplants



    world.update_sec()

    tik = tik + 1
    print(tik)
    #if tik == 100:
    #    world.vis(fname="100",collection=["Cactus","Hippophae","Thorn","Stipa"])
    #    with open('possibility.txt', 'w') as file:
    #        file.write(str(len(world.plants)/total)+" at day 100\n")

    #if tik == 200:
    #    world.vis(fname="200",collection=["Cactus","Hippophae","Thorn","Stipa"])
    #    with open('possibility.txt', 'a') as file:
    #        file.write(str(len(world.plants)/total)+" at day 200\n")

    log.append(len(world.plants)/total)
    if tik > 1000 or len(world.plants)==0 :
        break

   

    #if last_index is not None:
    #    print("The last element greater than 0.5 is at index:", last_index)
    #else:
    #    print("No element in the list is greater than 0.5")
    
world.vis(fname="final",collection=["Cactus","Hippophae","Thorn","Stipa"])


x_ax = range(0,len(log))

plt.figure(dpi=300).set_size_inches(8,6)
plt.plot(x_ax,log)
plt.xlabel("day")
plt.ylabel("survival possibility")
plt.title("Combination of 4 plants in desert climate")
plt.ylim(0,)
plt.xlim(0,)
plt.savefig("log.png")
print(coef)

#with open('data1.pkl', 'ab') as f:
#    pickle.dump(log, f)


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

def comp_4plants(a:float,b:float,c:float,d:float,total=300,logfile="log.png"):
    temperature,humidity,_ = simulate_tropical_savanna_climate_daily()
    plant_list = [1]*int(total*a) + [2]*int(total*b) + [3]*int(total*c) + [4]*int(total*d)

    world=init_sp(plant_list)
    tik = 0

    world.vis(fname="start",collection=["Cactus","Hippophae","Thorn","Stipa"])
    log = []
    while 1:
        climate = Climate(temperature[tik%360],humidity[tik%360])
        plants_iteration()
        for section in world.sections:
            sec_itr(section,climate)
        newplants = []
        for plant in world.plants:
            if plant.age % plant.repro_period == 0:
                sec = world.sections[plant.get_sec()]
                if sec.sil_hum > 200 and sec.nut > 200 and random.random() > 0.95:
                    newplants.append(spawn(plant))
                    sec.sil_hum = sec.sil_hum - 100
                    sec.nut = sec.nut - 100
                #print("New plant spawned!")
        world.plants = world.plants + newplants

        world.update_sec()

        tik = tik + 1
        print(tik)
        #if tik == 100:
            #world.vis(fname="100",collection=["Cactus","Hippophae","Thorn","Stipa"])
        #    with open('possibility.txt', 'w') as file:
        #        file.write(str(len(world.plants)/total)+" at day 100\n")

        #if tik == 200:
        #    #world.vis(fname="200",collection=["Cactus","Hippophae","Thorn","Stipa"])
        #    with open('possibility.txt', 'a') as file:
        #       file.write(str(len(world.plants)/total)+" at day 200\n")

        #log.append(len(world.plants)/total)
        if tik > 800 or len(world.plants)==0 :
            return
            break
    
    world.vis(fname="final",collection=["Cactus","Hippophae","Thorn","Stipa"])

    x_ax = range(0,len(log))

    plt.figure(dpi=300).set_size_inches(8,6)
    plt.plot(x_ax,log)
    plt.xlabel("day")
    plt.ylabel("survival possibility")
    plt.title("Combination of 4 plants")
    plt.ylim(0,)
    plt.xlim(0,)
    plt.savefig(logfile)
